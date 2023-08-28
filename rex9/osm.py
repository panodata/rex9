"""
Use OSM to find spots (amenities, features) of interest within walking distance.

Setup:

  pip install geopandas networkx osmnx pandas scikit-learn shapely

Resources:
- https://wiki.openstreetmap.org/wiki/Key:amenity
- https://github.com/gboeing/osmnx-examples/blob/v0.13.0/notebooks/13-isolines-isochrones.ipynb
- https://stackoverflow.com/questions/62789846/isochrones-with-osmnx
- https://github.com/gboeing/osmnx/issues/992
"""

import typing as t

import geopandas as gpd
import networkx as nx
import numpy as np
import osmnx as ox
from osmnx import features_from_polygon
from shapely import MultiPolygon
from shapely.geometry import Point, Polygon
from shapely.geometry.base import BaseGeometry


def setup():
    # pd.set_option("display.max_colwidth", 35)
    # pd.set_option('display.max_columns', 12)

    # ox.settings.log_console = True
    ox.settings.use_cache = True


TagsDict = t.Dict[str, t.Union[str, t.List[str]]]


class LocationFeatures:
    """
    Acquire location features from OSM, into a GeoDataFrame.
    """

    # For distance calculations, convert geometries to a coordinate system based on linear units (meters).
    # https://www.tomasbeuzen.com/python-for-geospatial-analysis/chapters/chapter1_intro-to-spatial.html
    crs_osm_default = ox.settings.default_crs  # EPSG:4326
    crs_metric = "EPSG:3347"

    # OSM features responses return many details. Let's skip a bunch of them.
    skip_columns = [
        # Restaurants
        "toilets:wheelchair",
        "wheelchair",
        "wheelchair:description",
        "wheelchair:description:de",
        "indoor_seating",
        "outdoor_seating",
        "delivery",
        "takeaway",
        "building",
        "diet:vegetarian",
        "drive_in",
        "internet_access:fee",
        "reservation",
        "smoking",
        "website",
        "nodes",
        "brand",
        "brand:wikidata",
        "brand:wikipedia",
        "operator",
        # Toilets
        "access",
        "changing_table",
        "toilets:disposal",
        "unisex",
    ]

    # Define a list of columns for a compact representation of the list of features.
    primary_columns = ["amenity", "cuisine", "name", "geometry", "address", "fee", "opening_hours"]
    very_compact_columns = ["distance", "amenity", "cuisine", "name", "address"]

    def __init__(self, center: Point, geometry: BaseGeometry, with_distance: bool = False):
        self.center = center
        self.geometry = geometry
        self.with_distance = with_distance

        # The OSM features, stored within a GeoDataFrame.
        self.features: t.Optional[gpd.GeoDataFrame] = None

        # Sanity checks.
        if not isinstance(self.geometry, (Polygon, MultiPolygon)):
            raise TypeError(f"Unable to compute features for geometry type: {type(self.geometry)}")

    def acquire(self, tags: TagsDict) -> None:
        """
        Query OSM Overpass API for features / tags.
        """
        assert isinstance(self.geometry, (Polygon, MultiPolygon))

        # Query OSM.
        self.features = features_from_polygon(self.geometry, tags=tags)

        # Some features are returned as polygons, like public toilet houses.
        # Just use the center coordinates, for a more compact representation.
        self.features["geometry"] = (
            self.features["geometry"].to_crs(self.crs_metric).centroid.to_crs(self.crs_osm_default)
        )

        # Converge address columns into a single one.
        self.compress_address()

        more_columns = self.features.columns.difference(self.primary_columns)
        f1 = gpd.GeoDataFrame(self.features, columns=self.primary_columns)
        f2 = gpd.GeoDataFrame(self.features, columns=more_columns)
        self.features = f1.join(f2)

        # Add a `distance` column, and sort data frame correspondingly.
        if self.with_distance:
            self.add_distance()

    def compress_address(self):
        """
        Compress address columns into single column.
        """
        features = self.features
        try:
            features["address"] = (
                features["addr:street"]
                + " "
                + features["addr:housenumber"]
                + ", "
                + features["addr:postcode"]
                + " "
                + features["addr:city"]
                + ", "
                + features["phone"]
            )
            features = features.drop(
                columns=["addr:street", "addr:housenumber", "addr:postcode", "addr:city", "addr:country", "phone"]
            )
            # features["address"] = features["address"].str.wrap(20)
        except:
            features["address"] = np.NaN
        self.features = features

    def add_distance(self) -> None:
        """
        Add a `distance` column, unit is meters, truncate to integer, and sort ascending.
        """
        center = gpd.points_from_xy([self.center.x], [self.center.y], crs=self.crs_osm_default).to_crs(self.crs_metric)
        self.features.insert(
            0, "distance", center.distance(self.features["geometry"].to_crs(self.crs_metric)).astype("int")
        )
        self.features = self.features.sort_values("distance")

    @property
    def full(self) -> gpd.GeoDataFrame:
        """
        Return the full GeoDataFrame.
        """
        if self.features is None:
            return gpd.GeoDataFrame()
        else:
            return self.features

    @property
    def compact(self) -> gpd.GeoDataFrame:
        # Skip a bunch of columns for a more compact representation.
        return self.full.drop(columns=self.skip_columns, errors="ignore")

    @property
    def very_compact(self) -> gpd.GeoDataFrame:
        """
        Return a compact representation of the data frame, defined by the list in `compact_columns`.
        Also drop the data frame index.
        """
        features = self.compact
        try:
            features = features[self.very_compact_columns]
            # return gpd.GeoDataFrame(self.features, columns=self.compact_columns)
            # return self.features[self.features.columns.intersection(take_columns)]
        except KeyError:
            pass
        return features.reset_index(drop=True)

    @property
    def super_compact(self) -> gpd.GeoDataFrame:
        """
        Use the compact representation, and additionally omit the `address` column.
        :return:
        """
        df = self.very_compact
        try:
            df = df.drop(columns=["address"])
            pass
        except:
            pass
        return df


class LocationOfInterest:
    def __init__(self, center: Point):
        self.center = center
        self.geometry: t.Optional[Polygon] = None
        self.queries: t.Dict[str, t.Dict] = {}
        self.configure_queries()

    def configure_queries(self):
        water = ["drinking_water", "shower", "water_point", "watering_place"]
        toilets_primary = ["toilets"]
        toilets_culture = ["cinema", "community_centre", "exhibition_centre", "library", "theatre", "university"]
        food = [
            "bar",
            "biergarten",
            "cafe",
            "fast_food",
            "food_court",
            "ice_cream",
            "internet_cafe",
            "nightclub",
            "pub",
            "restaurant",
        ]
        self.queries["water"] = {"amenity": water}
        self.queries["food"] = {"amenity": food}
        self.queries["toilet"] = {"amenity": toilets_primary + toilets_culture}

    def compute_isochrone(self, walk_time=5, speed=4.5):
        """
        https://stackoverflow.com/questions/62789846/isochrones-with-osmnx
        """
        loc = (self.center.y, self.center.x)
        G = ox.graph_from_point(loc, simplify=True, network_type="walk")

        # Use this line if the coordinates system returned from polys is changed from the original (check which crs you are using)
        # G = ox.project_graph(G, to_crs="4483")

        gdf_nodes = ox.graph_to_gdfs(G, edges=False)
        x, y = gdf_nodes["geometry"].unary_union.centroid.xy
        center_node = ox.nearest_nodes(G, Y=y[0], X=x[0])

        # km per hour to m per minute times the minutes to walk
        walking_meters = walk_time * speed * 1000 / 60

        subgraph = nx.ego_graph(G, center_node, radius=walking_meters, distance="length")
        node_points = [Point(data["x"], data["y"]) for node, data in subgraph.nodes(data=True)]
        self.geometry = gpd.GeoSeries(node_points).unary_union.convex_hull

    def get_features(self, label: t.Optional[str] = None, tags: t.Optional[TagsDict] = None):
        effective_tags: t.Dict = {}
        if label:
            effective_tags.update(self.queries[label])
        if tags:
            effective_tags.update(tags)
        location_features = LocationFeatures(center=self.center, geometry=self.geometry, with_distance=True)
        try:
            location_features.acquire(tags=effective_tags)
        except:
            print(f"No features found with tags: {effective_tags}")
        return location_features


def main():
    point = Point(13.24932, 52.75389)
    loi = LocationOfInterest(center=point)
    loi.compute_isochrone()

    print("Water")
    water_features = loi.get_features(label="water")
    print(water_features.compact)

    print("Food")
    food_features = loi.get_features(label="food")
    print(food_features.compact)

    print("Toilet")
    toilet_features = loi.get_features(label="toilet")
    print(toilet_features.compact)


if __name__ == "__main__":
    setup()
    main()

# Copyright (c) 2023, The Panodata developers and contributors.
# Distributed under the terms of the AGPLv3 license, see LICENSE.
import io
import logging
from contextlib import redirect_stdout

import click as click
import markdown2
from rich.console import Console

from rex9.core import compute_journey, make_travelplan
from rex9.util.cli import boot_click, docstring_format_verbatim, split_list
from rex9.util.format import CliFormatter as cf

logger = logging.getLogger()


def help_plan():
    """
    Invoke route planning.

    Synopsis
    ========
    rex9 travel --from=Oranienburg --to=Stralsund --stops=Fürstenberg,Mildenberg --on=do-di
    """


@click.group()
@click.version_option(package_name="rex9")
@click.option("--verbose", is_flag=True, required=False, help="Turn on logging")
@click.option("--debug", is_flag=True, required=False, help="Turn on logging with debug level")
@click.pass_context
def cli(ctx: click.Context, verbose: bool, debug: bool):
    verbose = True
    return boot_click(ctx, verbose, debug)


@cli.command(
    "travel",
    help=docstring_format_verbatim(help_plan.__doc__),
    context_settings={"max_content_width": 120},
)
@click.option("--from", "origin", type=str, required=True)
@click.option("--to", "destination", type=str, required=True)
@click.option("--stops", "stops", type=str, required=False)
@click.option("--on", "when", type=str, required=False)
@click.option("--format", "_format", type=str, required=False, default="markdown")
@click.pass_context
def travel(ctx: click.Context, origin: str, destination: str, stops: str, when: str, _format: str):
    logger.info(f"Computing journey from {origin} to {destination}")
    plan = make_travelplan(origin, destination, split_list(stops), when)
    compute_journey(plan)

    c = Console(width=100, highlighter=None)

    buffer = io.StringIO()
    with redirect_stdout(buffer):
        print("# Travel plan\n")
        for segment in plan.segments:
            first_journey_date = segment.first_journey_date
            c.print(
                f"## Connections from {cf.loc_pri(segment.origin.name)} to {cf.loc_pri(segment.destination.name)} "
                f"on {cf.time_sec(segment.first_journey_date)}"
            )
            print()
            for journey in segment.travel_journeys:
                journey_date = ""
                if journey.date != first_journey_date:
                    journey_date = f" on {cf.time_sec(journey.date)}"
                c.print(f"### Duration {cf.time_pri(journey.duration)}{journey_date}")
                for segment in journey.segments:
                    remarks = ""
                    if segment.remarks:
                        remarks = "\n" + segment.remarks
                    c.print(f"- {cf.time_sec(segment.time)}, {segment.transport}; {segment.details}{remarks}")
                print()
            print()

    buffer.seek(0)
    markdown = buffer.read()

    if _format == "markdown":
        print(markdown)
    elif _format == "html":
        html_body = markdown2.markdown(markdown.encode("utf-8"))
        html = f"""
<html>
<head>
<meta charset="UTF-8">
</head>
<body>
{html_body}
</body>
</html>
        """
        print(html)
    else:
        raise ValueError(f"Unknown output format: {_format}")

# Copyright (c) 2023, The Panodata developers and contributors.
# Distributed under the terms of the AGPLv3 license, see LICENSE.

import contextlib

from pyhafas import HafasClient

from rex9.model import TimeMode


@contextlib.contextmanager
def query_for(client: HafasClient, mode: TimeMode):
    """
    Manipulate pyhafas client to search by arrival instead of departure,
    by toggling the `outFrwd` parameter to `False`.

    Currently, it is implemented by monkey-patching pyHaFAS.
    TODO: Submit corresponding patch to pyHaFAS.
    """

    format_journeys_request_original = client.profile.format_journeys_request

    try:

        def format_journeys_request(*args, **kwargs):
            retval = format_journeys_request_original(*args, **kwargs)
            if mode is TimeMode.DEPARTURE:
                retval["req"]["outFrwd"] = True
            elif mode is TimeMode.ARRIVAL:
                retval["req"]["outFrwd"] = False
            return retval

        client.profile.format_journeys_request = format_journeys_request
        yield
    finally:
        client.profile.format_journeys_request = format_journeys_request_original

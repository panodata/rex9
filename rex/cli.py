# Copyright (c) 2023, The Panodata developers and contributors.
# Distributed under the terms of the AGPLv3 license, see LICENSE.

import logging

import click as click

from rex.core import make_travelplan
from rex.util.cli import boot_click, docstring_format_verbatim, split_list

logger = logging.getLogger()


def help_plan():
    """
    Invoke route planning.

    Synopsis
    ========
    rex travel --from=Oranienburg --to=Kopenhagen --stops=Fürstenberg,Mildenberg --on=do-di
    """


@click.group()
@click.version_option(package_name="rex")
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
@click.pass_context
def travel(ctx: click.Context, origin: str, destination: str, stops: str, when: str):
    logger.info(f"Computing journey from {origin} to {destination}")
    make_travelplan(origin, destination, split_list(stops), when)

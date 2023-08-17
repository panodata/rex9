# Copyright (c) 2023, The Panodata developers and contributors.
# Distributed under the terms of the AGPLv3 license, see LICENSE.

from click.testing import CliRunner

from rex.cli import cli


def test_travel_example(caplog):
    """
    CLI test: Invoke example `rex travel` command.
    """
    runner = CliRunner()

    result = runner.invoke(
        cli,
        args="travel --from=Oranienburg --to=Kopenhagen --stops=Fürstenberg,Mildenberg --on=do-di",
        catch_exceptions=False,
    )
    assert result.exit_code == 0

    assert "Travel plan draft: Locations" in caplog.text

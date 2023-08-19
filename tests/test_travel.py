# Copyright (c) 2023, The Panodata developers and contributors.
# Distributed under the terms of the AGPLv3 license, see LICENSE.

from click.testing import CliRunner

from rex9.cli import cli


def test_travel_ascii(caplog):
    """
    CLI test: Invoke example `rex9 travel` command.
    """
    runner = CliRunner()

    result = runner.invoke(
        cli,
        args="travel --from=Oranienburg --to=Kopenhagen --stops=Fürstenberg,Mildenberg --on=do-di",
        catch_exceptions=False,
    )
    assert result.exit_code == 0

    assert "Travel plan draft: Locations" in caplog.text


def test_travel_html(caplog):
    """
    CLI test: Invoke example `rex9 travel` command with HTML output.
    """
    runner = CliRunner()

    result = runner.invoke(
        cli,
        args="travel --from=Oranienburg --to=Kopenhagen --stops=Fürstenberg,Mildenberg --on=do-di --format=html",
        catch_exceptions=False,
    )
    assert result.exit_code == 0

    assert "Travel plan draft: Locations" in caplog.text
    assert "<html>" in result.output

# Copyright (c) 2023, The Panodata developers and contributors.
# Distributed under the terms of the AGPLv3 license, see LICENSE.

from click.testing import CliRunner
from strip_ansi import strip_ansi

from rex9.cli import cli


def test_travel_ascii(caplog):
    """
    CLI test: Invoke example `rex9 travel` command.
    """
    runner = CliRunner()

    result = runner.invoke(
        cli,
        args="travel --from=Oranienburg --to=Stralsund --stops=Fürstenberg,Mildenberg --when=do-di",
        catch_exceptions=False,
    )
    assert result.exit_code == 0
    output = strip_ansi(str(result.output).replace("\n", ""))

    assert "Travel plan draft: Segments" in caplog.text
    assert "Fahrradmitnahme begrenzt möglich" in output
    assert "Gransee->Neubrandenburg: Information. Erfahrungsgemäß hat dieser Zug eine hohe Auslastung." in output
    assert (
        "Fürstenberg(Havel)->Neubrandenburg: Information. Erfahrungsgemäß hat dieser Zug eine hohe Auslastung."
        in output
    )


def test_travel_html(caplog):
    """
    CLI test: Invoke example `rex9 travel` command with HTML output.
    """
    runner = CliRunner()

    result = runner.invoke(
        cli,
        args="travel --from=Oranienburg --to=Stralsund --stops=Fürstenberg,Mildenberg --when=do-di --format=html",
        catch_exceptions=False,
    )
    assert result.exit_code == 0

    assert "Travel plan draft: Segments" in caplog.text
    assert "<html>" in result.output

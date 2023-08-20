# Copyright (c) 2023, The Panodata developers and contributors.
# Distributed under the terms of the AGPLv3 license, see LICENSE.


class CliFormatter:
    """
    A few helper functions for colorizing terminal output.
    """

    @staticmethod
    def loc_pri(value: str):
        return f"[bold yellow]{value}[/bold yellow]"

    @staticmethod
    def loc_sec(value: str):
        return f"[yellow]{value}[/yellow]"

    @staticmethod
    def time_pri(value: str):
        return f"[bold cyan]{value}[/bold cyan]"

    @staticmethod
    def time_sec(value: str):
        return f"[cyan]{value}[/cyan]"

    @staticmethod
    def warn(value: str):
        return f"[on red]{value}[/on red]"

    @staticmethod
    def attention(value: str):
        return f"[bold red]{value}[/bold red]"

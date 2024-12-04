# SPDX-FileCopyrightText: © 2024 Jimmy Fitzpatrick <jcfitzpatrick12@gmail.com>
# This file is part of SPECTRE
# SPDX-License-Identifier: GPL-3.0-or-later

import typer

from spectre_cli.commands import safe_request
from spectre_cli.commands import (
    TAG_HELP,
    PROCESS_TYPE_HELP,
    DAY_HELP,
    MONTH_HELP,
    YEAR_HELP,
    EXTENSIONS_HELP
)

delete_app = typer.Typer()

@delete_app.command()
def logs(
    process_type: str = typer.Option(None, "--process-type", help=PROCESS_TYPE_HELP),
    year: int = typer.Option(None, "--year", "-y", help=YEAR_HELP),
    month: int = typer.Option(None, "--month", "-m", help=MONTH_HELP),
    day: int = typer.Option(None, "--day", "-d", help=DAY_HELP),
) -> None:
    payload = {
        "process_type": process_type,
        "year": year,
        "month": month,
        "day": day
    }
    _ = safe_request("delete/logs", "DELETE", payload)
    typer.secho("Logs successfully deleted.")


@delete_app.command()
def chunk_files(tag: str = typer.Option(..., "--tag", "-t", help=TAG_HELP),
                extensions: list[str] = typer.Option(..., "--extension", "-e", help=EXTENSIONS_HELP),
                year: int = typer.Option(None, "--year", "-y", help=YEAR_HELP),
                month: int = typer.Option(None, "--month", "-m", help=MONTH_HELP),
                day: int = typer.Option(None, "--day", "-d", help=DAY_HELP),
) -> None:
    # delete.chunk_files(tag,
    #                    extensions,
    #                    year,
    #                    month,
    #                    day,
    #                    suppress_doublecheck)
    raise typer.Exit()


@delete_app.command()
def fits_config(tag: str = typer.Option(..., "--tag", "-t", help=TAG_HELP),
) -> None:
    # delete.fits_config(tag)
    raise typer.Exit()


@delete_app.command()
def capture_config(tag: str = typer.Option(..., "--tag", "-t", help=TAG_HELP),
) -> None:
    # delete.capture_config(tag)
    raise typer.Exit()






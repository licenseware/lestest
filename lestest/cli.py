import typer
from lestest import (
    Lestest,
    ToxCreator,
    PytestIniCreator,
    RequirementsCreator,
    UnittestCreator,
)


app = typer.Typer(
    name="Lestest CLI",
    help="""
    Useful CLI commands for unittest files generation
    """,
)


@app.command()
def generate(package: str = None):
    """Generate unittest files for all functions and classes from current directory packages"""

    lestest = Lestest(
        tox=ToxCreator(),
        pytestini=PytestIniCreator(),
        requirements=RequirementsCreator(),
        unittest=UnittestCreator(package or "app"),
    )

    lestest.generate()

    typer.echo("Generated unittest boilerplate files")


def cli_entrypoint():
    app()

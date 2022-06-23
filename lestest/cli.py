import typer
from lestest import Lestest, ToxCreator, PytestIniCreator, RequirementsCreator


app = typer.Typer(
    name="Lestest CLI",
    help="""
    Useful CLI commands for unittest files generation
    """,
)


@app.command()
def generate():
    """Generate unittest files for all functions and classes from current directory packages"""

    lestest = Lestest(
        tox=ToxCreator(),
        pytestini=PytestIniCreator(),
        requirements=RequirementsCreator(),
    )

    lestest.generate()

    typer.echo("Generated unittest boilerplate files")


@app.command()
def boilerplate():
    """Generate `lestest_templates` external templates folder which you can overwrite"""

    typer.echo("TODO Generating unittest files")


def cli_entrypoint():
    app()
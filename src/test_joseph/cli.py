import click
import uvicorn

from test_joseph.app import make_app

from . import __version__


@click.group()
@click.version_option(version=__version__, prog_name="joseph")
def main() -> None: ...


@main.command(name="serve")
@click.option(
    "--host",
    type=str,
    default="127.0.0.1",
    help="Bind socket to this host.",
    show_default=True,
)
@click.option(
    "--port",
    type=int,
    default=8000,
    help="Bind socket to this port. If 0, an available port will be picked.",
    show_default=True,
)
def start_application(host: str, port: int):
    app = make_app()
    uvicorn.run(app, host=host, port=port)

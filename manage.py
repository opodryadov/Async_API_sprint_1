import logging

import click

from src.core import logger, settings


@click.group()
def cli():
    pass


@cli.command("api")
def api():
    import uvicorn

    from src.main import app

    uvicorn.run(
        app,
        host=settings.project_host,
        port=settings.project_port,
        log_config=logger.LOGGING,
        log_level=logging.DEBUG,
    )


if __name__ == "__main__":
    cli()

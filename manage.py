import logging

import click

from src.core import base, logger


@click.group()
def cli():
    pass


@cli.command("api")
def api():
    import uvicorn

    from src.main import create_app

    uvicorn.run(
        create_app(),
        host=base.PROJECT_HOST,
        port=base.PROJECT_PORT,
        log_config=logger.LOGGING,
        log_level=logging.DEBUG,
    )


if __name__ == "__main__":
    cli()

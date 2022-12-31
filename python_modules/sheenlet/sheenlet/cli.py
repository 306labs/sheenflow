import logging
import os
from typing import Optional

import click
import uvicorn

import sheenflow._check as check
from sheenflow._cli.utils import get_instance_for_service
from sheenflow._cli.workspace import (
    get_workspace_process_context_from_kwargs,
    workspace_target_argument,
)
from sheenflow._cli.workspace.cli_target import WORKSPACE_TARGET_WARNING
from sheenflow._core.telemetry import START_DAGIT_WEBSERVER, log_action
from sheenflow._core.telemetry_upload import uploading_logging_thread
from sheenflow._core.workspace.context import WorkspaceProcessContext
from sheenflow._utils import DEFAULT_WORKSPACE_YAML_FILENAME
from sheenflow._utils.log import configure_loggers

from .app import create_app_from_workspace_process_context
from .version import __version__


def create_dagit_cli():
    return dagit  # pylint: disable=no-value-for-parameter


DEFAULT_SHEENLET_HOST = "127.0.0.1"
DEFAULT_SHEENLET_PORT = 3000

DEFAULT_DB_STATEMENT_TIMEOUT = 15000  # 15 sec
DEFAULT_POOL_RECYCLE = 3600  # 1 hr


@click.command(
    name="sheenlet",
    help=(
        "Run sheenlet. Loads a repository or pipeline/job.\n\n{warning}".format(
            warning=WORKSPACE_TARGET_WARNING
        )
        + (
            "\n\nExamples:"
            "\n\n1. sheenlet (works if .{default_filename} exists)"
            "\n\n2. sheenlet -w path/to/{default_filename}"
            "\n\n3. sheenlet -f path/to/file.py"
            "\n\n4. sheenlet -f path/to/file.py -d path/to/working_directory"
            "\n\n5. sheenlet -m some_module"
            "\n\n6. sheenlet -f path/to/file.py -a define_repo"
            "\n\n7. sheenlet -m some_module -a define_repo"
            "\n\n8. sheenlet -p 3333"
            "\n\nOptions can also provide arguments via environment variables prefixed with SHEENLET"
            "\n\nFor example, SHEENLET_PORT=3333 sheenlet"
        ).format(default_filename=DEFAULT_WORKSPACE_YAML_FILENAME)
    ),
)
@workspace_target_argument
@click.option(
    "--host",
    "-h",
    type=click.STRING,
    default=DEFAULT_SHEENLET_HOST,
    help="Host to run server on",
    show_default=True,
)
@click.option(
    "--port",
    "-p",
    type=click.INT,
    help="Port to run server on.",
    default=DEFAULT_SHEENLET_PORT,
    show_default=True,
)
@click.option(
    "--path-prefix",
    "-l",
    type=click.STRING,
    default="",
    help="The path prefix where Sheenlet will be hosted (eg: /sheenlet)",
    show_default=True,
)
@click.option(
    "--db-statement-timeout",
    help="The timeout in milliseconds to set on database statements sent "
    "to the DagsterInstance. Not respected in all configurations.",
    default=DEFAULT_DB_STATEMENT_TIMEOUT,
    type=click.INT,
    show_default=True,
)
@click.option(
    "--db-pool-recycle",
    help="The maximum age of a connection to use from the sqlalchemy pool without connection recycling. Set to -1 to disable. Not respected in all configurations.",
    default=DEFAULT_POOL_RECYCLE,
    type=click.INT,
    show_default=True,
)
@click.option(
    "--read-only",
    help="Start Sheenlet in read-only mode, where all mutations such as launching runs and "
    "turning schedules on/off are turned off.",
    is_flag=True,
)
@click.option(
    "--suppress-warnings",
    help="Filter all warnings when hosting Sheenlet.",
    is_flag=True,
)
@click.option(
    "--log-level",
    help="Set the log level for the uvicorn web server.",
    show_default=True,
    default="warning",
    type=click.Choice(
        ["critical", "error", "warning", "info", "debug", "trace"], case_sensitive=False
    ),
)
@click.version_option(version=__version__, prog_name="sheenlet")
def dagit(
    host,
    port,
    path_prefix,
    db_statement_timeout,
    db_pool_recycle,
    read_only,
    suppress_warnings,
    log_level,
    **kwargs,
):
    if suppress_warnings:
        os.environ["PYTHONWARNINGS"] = "ignore"

    with get_instance_for_service("sheenlet") as instance:
        # Allow the instance components to change behavior in the context of a long running server process
        instance.optimize_for_dagit(db_statement_timeout, db_pool_recycle)

        with get_workspace_process_context_from_kwargs(
            instance,
            version=__version__,
            read_only=read_only,
            kwargs=kwargs,
        ) as workspace_process_context:
            host_dagit_ui_with_workspace_process_context(
                workspace_process_context,
                host,
                port,
                path_prefix,
                log_level,
            )


def host_dagit_ui_with_workspace_process_context(
    workspace_process_context: WorkspaceProcessContext,
    host: Optional[str],
    port: int,
    path_prefix: str,
    log_level: str,
):
    check.inst_param(
        workspace_process_context, "workspace_process_context", WorkspaceProcessContext
    )
    host = check.opt_str_param(host, "host", "127.0.0.1")
    check.int_param(port, "port")
    check.str_param(path_prefix, "path_prefix")

    configure_loggers()
    logger = logging.getLogger("sheenlet")

    app = create_app_from_workspace_process_context(workspace_process_context, path_prefix)

    logger.info(
        "Serving sheenlet on http://{host}:{port}{path_prefix} in process {pid}".format(
            host=host, port=port, path_prefix=path_prefix, pid=os.getpid()
        )
    )
    log_action(workspace_process_context.instance, START_DAGIT_WEBSERVER)
    with uploading_logging_thread():
        uvicorn.run(
            app,
            host=host,
            port=port,
            log_level=log_level,
        )


cli = create_dagit_cli()


def main():
    # click magic
    cli(auto_envvar_prefix="SHEENLET")  # pylint:disable=E1120

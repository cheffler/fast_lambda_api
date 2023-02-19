from click import Choice, echo
from click.decorators import command, group, option
from .config import config
from .utils import load_app


@group
def cli():
    ...


@command(name="export")
@option(
    "-t",
    "--target",
    default=f"{config.default_directory}/{config.default_app_filename}",
    show_default=True,
    help="Directory and file in which the app is",
)
@option(
    "-a",
    "--app-name",
    default="app",
    show_default=True,
    help="Name of the app in the target file",
)
@option(
    "-d",
    "--output-dir",
    default=config.default_directory,
    show_default=True,
    help="The output directory for any exported files",
)
@option(
    "-n",
    "--file-name",
    default=config.default_export_filename,
    show_default=True,
    help="The base file name for all exports",
)
@option(
    "-f",
    "--format",
    type=Choice(["json", "yaml"], case_sensitive=False),
    default="yaml",
    help="The format of the outputted file",
)
def export_open_api_spec(
    target: str,
    app_name: str,
    output_dir: str,
    file_name: str,
    format: str,
) -> None:
    """
    Export the OpenAPI specification from the target application
    """
    echo(f"reading app from {target}:{app_name}")
    app = load_app(target, app_name)

    print(app)

    echo(f"Writing files to f{output_dir} with base file name of {file_name}.{format}")


cli.add_command(export_open_api_spec)


if __name__ == "__main__":
    cli()

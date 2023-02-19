from os import makedirs
from pathlib import Path
from typing import List

from click import Choice
from click.decorators import command, group, option

from .config import config
from .spec import format_spec, get_filtered_spec
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
@option(
    "--filter",
    type=str,
    multiple=True,
    help="""Create a spec only for paths that contain this value. The exported
    filename will contain the value, e.g. for `export --filter v1 ->
    openapi_spec.v1.yaml`.""",
)
def export_open_api_spec(
    target: str,
    app_name: str,
    output_dir: str,
    file_name: str,
    format: str,
    filter: List[str],
) -> None:
    """
    Export the OpenAPI specification from the target application

    The specification can be filtered by the content of the path using the
    flag --filter, this will create one or more specifications depending
    on the number of flags provided.

    For example, to create multiple specs for different API versions use:
    export --filter v1 --filter v2
    """
    specs = {}
    app = load_app(target, app_name)

    if filter and len(filter) > 0:
        for f in filter:
            specs[f] = get_filtered_spec(app, f)
    else:
        specs["default"] = app.openapi()

    target_dir: Path = Path(".") / output_dir
    makedirs(target_dir, exist_ok=True)

    name: str
    for name, spec in specs.items():
        spec_str: str = format_spec(spec, format)
        if name == "default":
            filename = f"{file_name}.{format}"
        else:
            name = name.strip("/")
            filename = f"{file_name}.{name}.{format}"

        (target_dir / filename).write_text(spec_str)


cli.add_command(export_open_api_spec)


if __name__ == "__main__":
    cli()

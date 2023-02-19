from typing import List


class Config:
    default_directory: str = "api"
    default_app_filename: str = "app.py"
    default_app_name: str = "app"

    default_export_filename: str = "openapi_spec"

    export_file_types: List[str] = ["json", "yaml"]
    default_json_spaces: int = 4
    default_yaml_spaces: int = 4


config: Config = Config()

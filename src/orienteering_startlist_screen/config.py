import os
import tomllib


pyproject_path = "./pyproject.toml"
if not os.path.isfile(pyproject_path):
    raise FileNotFoundError(f"{pyproject_path}")


def get_version():
    try:
        with open(pyproject_path, "rb") as f:
            data = tomllib.load(f)

        # first try with PEP 621 structure
        version = data.get("project", {}).get("version")
        if version:
            return version

        # for fallback with poetry specific structure
        version = data.get("tool", {}).get("poetry", {}).get("version")
        if version:
            return version

        # if both are missing
        return "X_X_X"
    except Exception as e:
        print(f"Failure while reading the version out of the pyproject.toml file: {e}")
        return "X_X_X"


organization_name = "lenz-exe"
organization_domain = "https://www.example.com"
application_name = "Orienteering-Startlist-Screen"
application_version = get_version()
application_abbreviation = "OSS"
application_language = "de_DE"
module_name = "orienteering_startlist_screen"

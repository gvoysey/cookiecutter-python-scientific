from pathlib import Path


# remove docopt-specific file
cli_tool = '{{ cookiecutter.cli_tool}}'
pkg_name = '{{ cookiecutter.package_name }}'

if cli_tool != "docopt":
    to_remove = Path.cwd()/pkg_name/'from_docopt.py'
    to_remove.unlink()

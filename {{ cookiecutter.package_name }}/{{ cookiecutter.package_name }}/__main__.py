{%if cookiecutter.cli_tool == "docopt"%}"""{{ cookiecutter.package_name }}.

Usage:
{{ cookiecutter.package_name }} -h | --help
{{ cookiecutter.package_name }} --version

Options:

 -h --help    Show this screen.
 --version    Show the version.
"""

import sys
from {{ cookiecutter.package_name }}.from_docopt import from_docopt
from {{ cookiecutter.package_name }} import __version__


def main(inputargs=None):
    """Main entry point of {{ cookiecutter.package_name }}"""
    if inputargs is None:
        inputargs = sys.argv[1:] if len(sys.argv) > 1 else ""
    args = from_docopt(argv=inputargs, docstring=__doc__, version=__version__)
{% elif cookiecutter.cli_tool == "click" %}import click
from {{ cookiecutter.package_name }} import __version__

@click.command()
@click.version_option(version=__version__)
def main():
    pass

{% endif %}
if __name__ == "__main__":
    main()

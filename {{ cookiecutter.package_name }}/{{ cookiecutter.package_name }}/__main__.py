{%if cookiecutter.cli_tool == "docopt"%}
"""{{ cookiecutter.package_name }}.

Usage:
{{ cookiecutter.package_name }} -h | --help
{{ cookiecutter.package_name }} --version

Options:

 -h --help    Show this screen.
 --version    Show the version.
"""

from {{ cookiecutter.package_name }} import from_docopt, __version__

def main(inputargs=None):
    """Main entry point of {{ cookiecutter.package_name }}"""
    if inputargs is None:
        inputargs = sys.argv[1:] if len(sys.argv) > 1 else ""
    args = from_docopt(argv=inputargs, docstring=__doc__, version=__version__)
{% elif cookiecutter.cli_tool == "click" %}
import click

@click.command()
def main():
    pass

{% endif %}
if __name__ == "__main__":
    main()






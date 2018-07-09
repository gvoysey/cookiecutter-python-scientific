{%if cookiecutter.cli_tool == "docopt"%}
"""{{ cookiecutter.project_slug }}.

Usage:
{{ cookiecutter.project_slug }} -h | --help
{{ cookiecutter.project_slug }} --version

Options:

 -h --help    Show this screen.
 --version    Show the version.
"""

from docopt import docopt


def main(inputargs=None)
    """Main entry point of {{ cookiecutter.project_slug }}"""
    if inputargs is None:
        input
{% elif cookiecutter.cli_tool == "click" %}
import click

@click.command()
def main():
    pass

{% endif %}
if __name__ == "__main__":
    main()






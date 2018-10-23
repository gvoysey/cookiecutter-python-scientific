from pathlib import Path
from subprocess import run, CalledProcessError
import shlex

pkg_name = '{{ cookiecutter.package_name }}'
repo = '{{ cookiecutter.url }}'


def clean_up_docopt():
    """If click is selected, remove docopt-specific files."""
    cli_tool = '{{ cookiecutter.cli_tool}}'
    if cli_tool != "docopt":
        to_remove = Path.cwd() / pkg_name / 'from_docopt.py'
        to_remove.unlink()


def set_markup_style():
    """Use either markdown or org-mode as the default markup language."""
    markup_language = '{{ cookiecutter.markup_language }}'
    if markup_language == "org":
        to_remove = Path.cwd() / 'README.md'
        to_remove.unlink()
    elif markup_language == "markdown":
        to_remove = Path.cwd() / 'README.org'
        to_remove.unlink()


def install_deps():
    """Install dependencies with pipenv"""
    pipenv_dev = run('pipenv install --dev'.split(), check=True)
    print('Installed dependencies and virtual environment. Type `pipenv shell` to activate later.')


def install_black():
    formatter = "{{ cookiecutter.formatter }}"
    do_install = "{{ cookiecutter.install_precommit_hooks }}"
    if formatter == "black" and do_install == "yes":
        run('pipenv run pre-commit install'.split(), check=True)
        print('installed black as a pre-commit hook.')
    if formatter != "black":
        run('pipenv uninstall black'.split(), check=True)
    if do_install == "no":
        run('pipenv uninstall pre-commit'.split(), check=True)


def init_repo():
    """Initialize a git repository for this project."""
    print(f"Initializing development environment for {pkg_name}")
    try:
        git_init = run('git init .'.split(), check=True)
        print('Initialized git repository')
        if repo:
            git_add_remote = run(f'git remote add origin {repo}'.split(), check=True)
            print(f'Found url, set origin: {repo}')
        git_add = run('git add -A'.split(), check=True)
        git_commit = run(shlex.split(f'git commit -m "first commit of {pkg_name} "'), check=True)
        git_tag = run(shlex.split('git tag -a -m "first tag" 0.0.1'), check=True)
        print('First commit.')
        pipenv_versioneer = run('pipenv run versioneer install'.split(), check=True)
        print('Installed versioneer')
        pipenv_install_dev = run('pipenv run pip install -e .'.split(), check=True)
        print('Installed package in development mode.')
        git_add_after = run('git add -A'.split(), check=True)
        git_commit_after = run(shlex.split('git commit -m "added versioneer support."'), check=True)
        print('second commit.')
        print('All set!')
    except CalledProcessError as e:
        print(e)


def main():
    clean_up_docopt()
    set_markup_style()

    install_deps()
    init_repo()
#    install_black()


if __name__ == "__main__":
    main()

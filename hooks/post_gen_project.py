from pathlib import Path
from subprocess import run, CalledProcessError
import shlex

pkg_name = '{{ cookiecutter.package_name }}'
repo = '{{ cookiecutter.url }}'

def clean_up_docopt():
    # remove docopt-specific file
    cli_tool = '{{ cookiecutter.cli_tool}}'
    if cli_tool != "docopt":
        to_remove = Path.cwd()/pkg_name/'from_docopt.py'
        to_remove.unlink()

def init_project():
    """Initialize a repo"""
    print(f"Initializing development environment for {pkg_name}")
    try:
        pipenv_dev = run('pipenv install --dev'.split(), check=True)
        print('Installed dependencies, created virtualenv.')
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
    init_project()

if __name__ == "__main__":
    main()

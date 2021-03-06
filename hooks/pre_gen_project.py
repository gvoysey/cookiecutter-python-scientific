import sys

MIN_PYTHON_VER = (3, 6)
if sys.version_info < MIN_PYTHON_VER:
    sys.exit("Python 3.6 or later is required!")
from subprocess import run, CalledProcessError


def check_prerequisites():
    try:
        run("git --version".split(), check=True)
    except CalledProcessError as e:
        print("git is required!")
        raise FileNotFoundError
    try:
        run("pipenv --version".split(), check=True)
    except CalledProcessError as e:
        print("pipenv is required!")
        res = input("Attempt to install pipenv? [Y/n]: ")
        if not res or res.casefold() == "y":
            try:
                pipenv_install = run("pip install --user pipenv".split(), check=True)
            except CalledProcessError:
                raise FileNotFoundError
        else:
            raise FileNotFoundError


def main():
    check_prerequisites()


if __name__ == "__main__":
    main()

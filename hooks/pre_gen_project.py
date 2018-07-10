import sys
if sys.version_info[:2] < (3,6):
    sys.exit('Python 3.6 or later is required!')
from subprocess import run, CalledProcessError

def check_prerequisites():
    try:
        run('git --version'.split(), check=True)
    except CalledProcessError as e:
        print('git is required!')

    try:
        run('pipenv --version'.split(), check=True)
    except CalledProcessError as e:
        print('pipenv is required!')

def main():
    check_prerequisites()

if __name__ == "__main__":
    main()

import os
import shutil
from pathlib import Path

cli_tool = '{{ cookiecutter.cli_tool}}'

if cli_tool != "docopt":
    to_remove = Path.cwd()/'from_docopt.py'
    to_remove.unlink()
    

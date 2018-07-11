import subprocess
from jinja2 import Environment
from jinja2.ext import Extension


class NameExt(Extension):
    def __init__(self, environment):
        super(NameExt, self).__init__(environment)
        environment.globals['name'] = subprocess.check_output('whoami').strip()

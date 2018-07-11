import pytest
import hypothesis

import {{ cookiecutter.package_name }}

def test_{{ cookiecutter.package_name }}_version():
    """Test that the package exists and has a version"""
    assert {{cookiecutter.package_name }}.__version__


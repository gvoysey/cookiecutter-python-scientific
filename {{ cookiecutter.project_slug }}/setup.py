from setuptools import setup, find_packages
import versioneer


setup(
    name='{{ cookiecutter.project_slug }}'
    , packages=find_packages()
    , version=versioneer.get_version()
    , cmdclass=versioneer.get_cmdclass()
    , entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_slug }} = {{ cookiecutter.project_slug }}.__main__:main'
        ]
    }
    , url='{{ cookiecutter.url }}'
    , author='{{ cookiecutter.full_name }}'
    , author_email='{{ cookiecutter.email }}'
    , description='{{ cookiecutter.project_tagline }}'
    , install_requires=[
                        'attrs'
                        , 'numpy'
                        , 'versioneer'
                        {% if cookiecutter.cli_tool == "docopt" %}, 'docopt'{% elif cookiecutter.cli_tool == "click" %}, 'click'{% endif %}
                        ]
    , tests_require=[
                     'hypothesis'
                     , 'pytest'
                    ]
    , test_suite='pytest'
)

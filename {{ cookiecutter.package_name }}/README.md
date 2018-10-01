# Introduction
{{ cookiecutter.package_name }} is {{ cookiecutter.project_description }}. 
# Use
# Requirements
{% if cookiecutter.url and 'github' in cookiecutter.url %}
# Installation
## From Github
To obtain the latest version of this package:
```
pip install git+{{ cookiecutter.url }}
```

## Development
If you wish to work on this project locally, clone this repo and install it in
development mode:

```
git clone {{ cookiecutter.url }}
cd {{ cookiecutter.package_name }}
make dev
```
{% endif %}

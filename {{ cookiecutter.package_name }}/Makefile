all:
	@echo "\t\`make test\` to run tests"
	@echo "\t\`make dev\` to install development version"
	@echo "\t\`make lint\` to run static typing tests"

init:
	@echo "initializing development environment for {{ cookiecutter.package_name }}"
	@pipenv install --dev
	@git init .
	@git add -A && git commit -m "first commit of {{ cookiecutter.package_name }}, a {{ cookiecutter.project_tagline }}."
	@git tag -a -m "first tag" 0.0.1
	@pipenv run versioneer install
	@pipenv run pip install -e .
	@git add -A && git commit -m "added versioneer support."
	@echo "Finished initialization.  Run pipenv shell to enter an activated virtual environment, make test to run tests, make lint to run linters."

dev :
	@pipenv install --dev
	@pipenv run pip install -e .
	@echo "installed development version; run \`pipenv shell\` to enter activated environment."

test:
	@pipenv run pytest --cov-report term-missing --cov={{ cookiecutter.package_name }} tests/


lint :
	@echo "======== PYLINT ======="
	@pipenv run pylint --rcfile=.pylintrc {{ cookiecutter.package_name }} -f parseable -r n
	@echo "======== MYPY ======="
	@pipenv run mypy --ignore-missing-imports --follow-imports=skip {{ cookiecutter.package_name }}
	@echo "======== PYCODESTYLE ======="
	@pipenv run pycodestyle {{ cookiecutter.package_name }} --max-line-length=120
	@echo "======== PYDOCSTYLE  ======="
	@pipenv run pydocstyle {{ cookiecutter.package_name }}

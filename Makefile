.PHONY: lint test coverage clean

lint:
	@flake8 cermin

test:
	@nosetests --nologcapture

coverage:
	@rm -f .coverage
	@nosetests --with-coverage --cover-package=dss

clean: clean-pyc clean-coverage

clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +

clean-coverage:
	@rm -rf cover
	@rm -f .coverage

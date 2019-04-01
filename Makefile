TARGET_FILE = hc_upgrade.tar.gz
BUILD_DIR = build

PIP_CMD ?= pip
PY3 ?= python3
VENV_DIR ?= venv
VENV_RUN = . $(VENV_DIR)/bin/activate

usage:		## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'


build:	clean install		## Build the upgrade package.


install:		## Install dependencies in virtualenv
	$(PY3) -m venv --copies $(VENV_DIR) ; \
	$(VENV_RUN); $(PIP_CMD) -q install -r requirements.txt ; \
	sed -i "s|\"OLD_DIR_PATH\"|$(pwd)|" prepare.sh; \
	mkdir $(BUILD_DIR) && tar -zcf $(BUILD_DIR)/$(TARGET_FILE) .



clean:		## Clear all the .pyc/.pyo files and virtual env files.
	rm -rf $TARGET_FILE $(VENV_DIR) $(BUILD_DIR) __pycache__ .idea .pytest_cache
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +


test:	clean		## Run automated tests.
	python -m pytest -v tests/


lint:		## Run code linter to check code style.
	flake8 --inline-quotes=single --show-source --max-line-length=120 --ignore=E128,W504 --exclude=./migration


.PHONY: usage install clean lint run test

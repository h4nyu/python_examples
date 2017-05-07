# -*- coding: utf-8 -*-
# Need virtualenv
.PHONY: all clean build database pip restore

all: build
	@echo "build finished..."

build: pip 

test:
	python setup.py test
pip:
	pip install pip-tools
	pip-compile requirements.in
	pip-compile dev-requirements.in
	pip-sync requirements.txt dev-requirements.txt

PHONY: run


PYTHON=.venv/bin/python
PIP=.venv/bin/pip

make-venv:
	python3 -m venv .venv

install:
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) main.py
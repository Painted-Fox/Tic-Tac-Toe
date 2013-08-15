PYTHON = python
TESTRUNNER = unittest
RUNTEST = $(PYTHON) -m $(TESTRUNNER)

all: run

run::
	$(PYTHON) yaktak/app.py

test::
	$(RUNTEST) yaktak.tests.test_suite

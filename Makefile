PYTHON = python
TESTRUNNER = unittest
RUNTEST = $(PYTHON) -m $(TESTRUNNER)

all: run

run::
	$(PYTHON) run.py

test::
	$(RUNTEST) yaktak.tests.test_suite

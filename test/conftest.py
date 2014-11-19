from __future__ import print_function

from coverage import coverage

cov = coverage(source=('doubles',))
cov.start()

from doubles.pytest import pytest_runtest_call  # noqa


def pytest_sessionfinish(session, exitstatus):
    cov.stop()
    cov.save()


def pytest_terminal_summary(terminalreporter):
    print("\nCoverage report:\n")
    cov.report(show_missing=True, ignore_errors=True, file=terminalreporter._tw)
    cov.html_report()

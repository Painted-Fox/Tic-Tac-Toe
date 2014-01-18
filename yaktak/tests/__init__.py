"""
Unit tests for yaktak.
"""

import unittest

def test_suite():
    """Unit test suite."""

    result = unittest.TestSuite()
    names = [
        'wopr',
        'board',
        ]
    module_names = ['yaktak.tests.test_' + name for name in names]
    loader = unittest.TestLoader()
    result.addTests(loader.loadTestsFromNames(module_names))
    return result

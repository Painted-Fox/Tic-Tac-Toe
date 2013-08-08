import unittest

def test_suite():
    result = unittest.TestSuite()
    names = [
        'board',
        ]
    module_names = ['yaktak.tests.test_' + name for name in names]
    loader = unittest.TestLoader()
    result.addTests(loader.loadTestsFromNames(module_names))
    return result

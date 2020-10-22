"""
You can auto-discover and run all tests with this command:

    py.test

Documentation: https://docs.pytest.org/en/latest/
"""

# import the main module
from main import isLeapYear


def test_isLeapYear_test1(year = 2020):
    assert isLeapYear(year) == 'Could be a leap year.'

def test_isLeapYear_test2(year = 2021):
    assert isLeapYear(year) == 'Definitely not a leap year.'

def test_isLeapYear_test3(year = 2016):
    assert isLeapYear(year) == 'Could be a leap year.'

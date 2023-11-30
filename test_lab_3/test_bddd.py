# tests/test_my_feature.py
from pytest_bdd import scenarios, parsers, scenario, given, when, then
from pathlib import Path
from test_lab_3.Calcul import Calculator
import pytest

cal = Calculator()
featureFileDir = 'features'
feauterFile = 'calculator.feature'
Base_Dir = Path(__file__).resolve().parent
Feature_file = Base_Dir.joinpath(featureFileDir).joinpath(feauterFile)

def pytest_configure():
    pytest.a = 0
    pytest.b = 0
    pytest.result = 0

@scenario(Feature_file, 'Add two numbers')
def test_withdrawal():
    print('\ntest passed')

@given('I have a calculator')
def current_balance():
    pytest.a = 5
    pytest.b = 7

@when('I add 5 and 7')
def winthdraw_amount():
    pytest.result = cal.sum(pytest.a, pytest.b)

@then('the result should be 12')
def final_balance():
    assert pytest.result == 12


@scenario(Feature_file, 'Diff two numbers')
def test_withdrawal():
    print('\ntest passed')

@given('I have a calculator')
def current_balance():
    pytest.a = 5
    pytest.b = 7

@when('I diff 5 and 7')
def winthdraw_amount():
    pytest.result = cal.subtract(pytest.a, pytest.b)

@then('the result should be -2')
def final_balance():
    assert pytest.result == -2



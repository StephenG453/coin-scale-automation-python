from pytest_bdd import scenarios, scenario, given, when, then
from selenium_framework.pages.home_page import HomePage
from selenium import webdriver
from pytest_bdd.parsers import parse
import pytest

# scenario('../test_happy_path.feature', 'test functionality of locating a fake weight inside the React App')
# scenarios('../test_happy_path.feature')


# @pytest.mark.usefixtures("webdriver_setup")
# class HomePageStepDefinitions:

@scenario('../test_happy_path.feature', 'test functionality of locating a fake weight inside the React App')
def test_app():
    pass

# @given(parse('React Application is loaded and home page is visible'))
@given('React Application is loaded and home page is visible')
def initialize_driver_and_open_react_app(webdriver_setup):
    home_page = HomePage(webdriver_setup)
    home_page.load()

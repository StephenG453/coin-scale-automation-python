from pytest_bdd import scenarios, scenario, given, when, then
from selenium_framework.pages.home_page import HomePage

import time

@scenario('../test_happy_path.feature', 'test functionality of locating a fake weight inside the React App')
def test_app():
    pass

@given('React Application is loaded and home page is visible')
def initialize_driver_and_open_react_app(webdriver_setup):
    print("inside initialize_driver_and_open_react_app")
    home_page = HomePage(webdriver_setup)
    home_page.load()

    # time.sleep(10)



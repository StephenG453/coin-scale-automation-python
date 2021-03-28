from pytest_bdd import scenarios, scenario, given, when, then
from selenium_framework.pages.home_page import HomePage
from selenium import webdriver

import time

@scenario('../test_happy_path.feature', 'test functionality of locating a fake weight inside the React App')
def test_app():
    pass


# driver = webdriver
# home_page = HomePage

@given('React Application is loaded and home page is visible')
def initialize_driver_and_open_react_app(webdriver_setup):
    print("inside initialize_driver_and_open_react_app\n")
    driver = webdriver_setup
    home_page = HomePage(driver)
    home_page.load()

    # print("driver current URL is:", driver.current_url, "\n")

    # time.sleep(10)


@when('coin 0 is added to first cell in the left grid')
def input_coin_zero_into_left_grid(webdriver_setup):
    home_page = HomePage(webdriver_setup)
    home_page.insert_coin_into_left_grid(coin=0, cell=0)


@when('coin 1 is added to second cell in the left grid')
def input_coin_one_into_left_grid(webdriver_setup):
    home_page = HomePage(webdriver_setup)
    home_page.insert_coin_into_left_grid(coin=1, cell=1)


@when('coin 2 is added to third cell in the left grid')
def input_coin_two_into_left_grid(webdriver_setup):
    home_page = HomePage(webdriver_setup)
    home_page.insert_coin_into_left_grid(coin=2, cell=2)


@when('coin 3 is added to first cell in the right grid')
def input_coin_three_into_right_grid(webdriver_setup):
    home_page = HomePage(webdriver_setup)
    home_page.insert_coin_into_right_grid(coin=3, cell=0)


@when('coin 4 is added to second cell in the right grid')
def input_coin_three_into_right_grid(webdriver_setup):
    home_page = HomePage(webdriver_setup)
    home_page.insert_coin_into_right_grid(coin=4, cell=1)


@when('coin 5 is added to third cell in the right grid')
def input_coin_three_into_right_grid(webdriver_setup):
    home_page = HomePage(webdriver_setup)
    home_page.insert_coin_into_right_grid(coin=5, cell=2)


@when('weigh button is pressed')
def press_weight_button(webdriver_setup):
    home_page = HomePage(webdriver_setup)
    home_page.press_weigh_button()

    time.sleep(2)

# from pytest_bdd import scenarios, scenario, given, when, then
from selenium_framework.pages.home_page import HomePage
from selenium import webdriver

import time

from behave import *
from behave import use_fixture


# @scenario('../happy_path.feature', 'test functionality of locating a fake weight inside the React App')
# def test_app():
#     pass


# driver = webdriver
# home_page = HomePage

@given('React Application is loaded and home page is visible')
# 2fixture(use_fixture(webdriver_setup)
def initialize_driver_and_open_react_app(context):
    print("inside initialize_driver_and_open_react_app\n")
    driver = context.browser
    home_page = HomePage(driver)
    home_page.load()

    # print("driver current URL is:", driver.current_url, "\n")

    # time.sleep(10)


# TODO parameterize gherkin steps
@when('user adds coin {int1} into cell {int2} in the {str} grid')
def insert_coin_into_cell_in_grid(context, int1, int2, str):
    driver = context.browser
    home_page = HomePage(driver)
    if 'left' in str:
        home_page.insert_coin_into_left_grid(coin=int1, cell=int2)
    elif 'right' in str:
        home_page.insert_coin_into_right_grid(coin=int1, cell=int2)


@when('user adds coin 0 to first cell in the left grid')
def input_coin_zero_into_left_grid(webdriver_setup):
    home_page = HomePage(webdriver_setup)
    home_page.insert_coin_into_left_grid(coin=0, cell=0)


@when('user adds coin 1 to second cell in the left grid')
def input_coin_one_into_left_grid(webdriver_setup):
    home_page = HomePage(webdriver_setup)
    home_page.insert_coin_into_left_grid(coin=1, cell=1)


@when('user adds coin 2 to third cell in the left grid')
def input_coin_two_into_left_grid(webdriver_setup):
    home_page = HomePage(webdriver_setup)
    home_page.insert_coin_into_left_grid(coin=2, cell=2)


@when('user adds coin 3 to first cell in the right grid')
def input_coin_three_into_right_grid(webdriver_setup):
    home_page = HomePage(webdriver_setup)
    home_page.insert_coin_into_right_grid(coin=3, cell=0)


@when('user adds coin 4 to second cell in the right grid')
def input_coin_three_into_right_grid(webdriver_setup):
    home_page = HomePage(webdriver_setup)
    home_page.insert_coin_into_right_grid(coin=4, cell=1)


@when('user adds coin 5 to third cell in the right grid')
def input_coin_three_into_right_grid(webdriver_setup):
    home_page = HomePage(webdriver_setup)
    home_page.insert_coin_into_right_grid(coin=5, cell=2)


@when('user presses weigh button')
def press_weigh_button(webdriver_setup):
    home_page = HomePage(webdriver_setup)
    home_page.press_weigh_button()


@when('user checks latest weight result')
def check_latest_weigh_result(webdriver_setup):
    home_page = HomePage(webdriver_setup)
    home_page.check_latest_weigh_results()


@when('user clears right grid')
def clear_right_grid(webdriver_setup):
    home_page = HomePage(webdriver_setup)
    home_page.clear_grid('r')


@when('user adds coin 6 to first cell in the right grid')
def input_coin_six_into_right_grid(webdriver_setup):
    home_page = HomePage(webdriver_setup)
    home_page.insert_coin_into_right_grid(coin=6, cell=0)


@when('user adds coin 7 to second cell in the right grid')
def input_coin_seven_into_right_grid(webdriver_setup):
    home_page = HomePage(webdriver_setup)
    home_page.insert_coin_into_right_grid(coin=7, cell=1)


@when('user adds coin 8 to third cell in the right grid')
def input_coin_eight_into_right_grid(webdriver_setup):
    home_page = HomePage(webdriver_setup)
    home_page.insert_coin_into_right_grid(coin=8, cell=2)


@when('user determines group with fake weight')
def determine_group_with_fake_weight(webdriver_setup):
    home_page = HomePage(webdriver_setup)
    home_page.determine_group_with_fake_weight()


@then('user finds fake weight')
def locate_fake_weight(webdriver_setup):
    home_page = HomePage(webdriver_setup)
    home_page.locate_fake_weight_within_group()

    # time.sleep(10)

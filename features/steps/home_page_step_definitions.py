# from pytest_bdd import scenarios, scenario, given, when, then
from pages.home_page import HomePage

from behave import *


@given('React Application is loaded and home page is visible')
def initialize_driver_and_open_react_app(context):
    driver = context.browser
    home_page = HomePage(driver)
    home_page.load()


@step('user adds coin {int1} into cell {int2} in the {str} grid')
def insert_coin_into_cell_in_grid(context, int1, int2, str):
    driver = context.browser
    home_page = HomePage(driver)
    if 'left' in str:
        home_page.insert_coin_into_left_grid(coin=int1, cell=int2)
    elif 'right' in str:
        home_page.insert_coin_into_right_grid(coin=int1, cell=int2)


@step('user adds a coin into a cell in a grid')
def insert_coin_into_cell_in_grid(context):
    driver = context.browser
    home_page = HomePage(driver)

    for row in context.table:
        if 'left' in row['grid']:
            home_page.insert_coin_into_left_grid(coin=row['coin'], cell=row['cell'])
        elif 'right' in row['grid']:
            home_page.insert_coin_into_right_grid(coin=row['coin'], cell=row['cell'])


@step('user presses weigh button')
def press_weigh_button(context):
    driver = context.browser
    home_page = HomePage(driver)
    home_page.press_weigh_button()


@step('user checks latest weight result')
def check_latest_weigh_result(context):
    driver = context.browser
    home_page = HomePage(driver)
    home_page.check_latest_weigh_results()


@step('user clears right grid')
def clear_right_grid(context):
    driver = context.browser
    home_page = HomePage(driver)
    home_page.clear_grid('r')


@step('user determines group with fake weight')
def determine_group_with_fake_weight(context):
    driver = context.browser
    home_page = HomePage(driver)
    home_page.determine_group_with_fake_weight()


@step('user finds fake weight')
def locate_fake_weight(context):
    driver = context.browser
    home_page = HomePage(driver)
    home_page.locate_fake_weight_within_group()

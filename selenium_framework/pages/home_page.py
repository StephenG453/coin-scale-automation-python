from selenium.webdriver.common.by import By
from selenium_framework.pages.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement


class HomePage(BasePage):
    URL = 'http://ec2-54-208-152-154.compute-1.amazonaws.com/'

    WEIGH_BUTTON = (By.ID, 'weigh')

    def __init__(self, driver):
        super().__init__(driver)
        # self.browser = browser

    def load(self):
        self.driver.get(self.URL)

    def insert_coin_into_left_grid(self, coin: int, cell: int):
        coin_to_be_inserted = self.driver.find_element_by_id('coin_' + str(coin)).text
        cell_to_be_filled = self.driver.find_element_by_id('left_' + str(cell))
        cell_to_be_filled.send_keys(coin_to_be_inserted)

    def insert_coin_into_right_grid(self, coin: int, cell: int):
        coin_to_be_inserted = self.driver.find_element_by_id('coin_' + str(coin)).text
        cell_to_be_filled = self.driver.find_element_by_id('right_' + str(cell))
        cell_to_be_filled.send_keys(coin_to_be_inserted)

    def press_weigh_button(self):
        self.driver.find_element(*self.WEIGH_BUTTON).click()

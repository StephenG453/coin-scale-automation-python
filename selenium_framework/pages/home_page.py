from selenium.webdriver.common.by import By
from selenium_framework.pages.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys


class HomePage(BasePage):
    URL = 'http://ec2-54-208-152-154.compute-1.amazonaws.com/'

    WEIGH_BUTTON = (By.ID, 'weigh')
    WEIGHINGS = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[5]")

    is_round_one_result_equal = False
    is_round_two_result_equal = False

    is_fake_weight_in_group_one = False
    is_fake_weight_in_group_two = False
    is_fake_weight_in_group_three = False

    def __init__(self, driver):
        super().__init__(driver)

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

    def check_latest_weigh_results(self):
        current_weighings = self.driver.find_element(*self.WEIGHINGS)
        list_of_weighs = current_weighings.find_elements_by_tag_name('li')

        # round 1
        if len(list_of_weighs) == 1:
            latest_web_element = list_of_weighs[0]
            text = latest_web_element.text

            if '=' in text:
                self.is_round_one_result_equal = True

        # round 2
        elif len(list_of_weighs):
            latest_web_element = list_of_weighs[1]
            text = latest_web_element.text

            if '=' in text:
                self.is_round_two_result_equal = True

    def determine_group_with_fake_weight(self):
        if self.is_round_one_result_equal:
            if self.is_round_two_result_equal:
                self.is_fake_weight_in_group_one = True
            else:
                self.is_fake_weight_in_group_three = True
        else:
            if self.is_round_two_result_equal:
                self.is_fake_weight_in_group_two = True
            else:
                self.is_fake_weight_in_group_one = True

    def clear_grid(self, grid: str):
        if grid != 'r' and grid != 'l':
            print("Please enter 'l' to clear left grid or 'r' to clear right grid.")
            # super(HomePage, self).driver.close()

        n = 9
        if grid == 'r':
            for i in range(n):
                cell_to_be_cleared = self.driver.find_element_by_id('right_' + str(i))
                cell_to_be_cleared.send_keys(Keys.BACK_SPACE)
        elif grid == 'l':
            for i in range(n):
                cell_to_be_cleared = self.driver.find_element_by_id('left_' + str(i))
                cell_to_be_cleared.send_keys(Keys.BACK_SPACE)
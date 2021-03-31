from selenium.webdriver.common.by import By
from selenium_framework.pages.base_page import BasePage
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
                HomePage.is_round_one_result_equal = True

        # round 2
        elif len(list_of_weighs):
            latest_web_element = list_of_weighs[1]
            text = latest_web_element.text

            if '=' in text:
                HomePage.is_round_two_result_equal = True

    @staticmethod
    def determine_group_with_fake_weight():
        if HomePage.is_round_one_result_equal:
            if HomePage.is_round_two_result_equal:
                HomePage.is_fake_weight_in_group_one = True
            else:
                HomePage.is_fake_weight_in_group_three = True
        else:
            if HomePage.is_round_two_result_equal:
                HomePage.is_fake_weight_in_group_two = True
            else:
                HomePage.is_fake_weight_in_group_one = True

    def locate_fake_weight_within_group(self):
        n = 3
        if HomePage.is_fake_weight_in_group_one:
            for weight in range(n):
                self.driver.find_element_by_id('coin_' + str(weight)).click()

                alert = self.driver.switch_to.alert
                print("alert text is: " + alert.text)

                if 'Yay!' in alert.text:
                    print('fake weight is coin ' + str(weight))
                    alert.accept()
                    break
                alert.accept()
        elif HomePage.is_fake_weight_in_group_two:
            n = 6
            for weight in range(3, n):
                self.driver.find_element_by_id('coin_' + str(weight)).click()

                alert = self.driver.switch_to.alert
                print("alert text is: " + alert.text)

                if 'Yay!' in alert.text:
                    print('fake weight is coin ' + str(weight))
                    alert.accept()
                    break
                alert.accept()
        else:
            n = 9
            for weight in range(6, n):
                self.driver.find_element_by_id('coin_' + str(weight)).click()

                alert = self.driver.switch_to.alert
                print("alert text is: " + alert.text)

                if 'Yay!' in alert.text:
                    print('fake weight is coin ' + str(weight))
                    alert.accept()
                    break
                alert.accept()

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

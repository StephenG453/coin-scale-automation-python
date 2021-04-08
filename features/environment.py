import pytest

from behave import fixture

from selenium import webdriver


# # TODO make sure session is the accurate scope
# # @pytest.fixture(scope="session")
# @fixture
# def webdriver_setup(request):
#     """
#     This function sets up and tears down the webdriver after every session
#     """
#     options = webdriver.ChromeOptions()
#     options.add_argument('--ignore-ssl-errors=yes')
#     options.add_argument('--ignore-certificate-errors')
#     driver = webdriver.Chrome(options=options)
#     driver.set_page_load_timeout(15)
#     driver.maximize_window()
#
#     yield driver
#     driver.close()

def before_all(context):
    print("inside before_all\n")
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    # context = webdriver.Chrome(options=options)
    # context.set_page_load_timeout(15)
    # context.maximize_window()
    context.browser = webdriver.Chrome(options=options)

    # yield context
    # context.close()


# def after_all(context):
#     print(context)
#     print("inside after_all\n")
#     context.browser.quit()

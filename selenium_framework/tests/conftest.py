import pytest

from selenium import webdriver


@pytest.fixture(scope="session")
def webdriver_setup(request):
    """
    This function sets up and tears down the webdriver after every class
    """
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(15)
    driver.maximize_window()

    yield driver
    driver.close()

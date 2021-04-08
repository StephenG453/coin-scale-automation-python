from selenium import webdriver


def before_all(context):
    print("inside before_all\n")
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    context.browser = webdriver.Chrome(options=options)
    context.browser.maximize_window()
    context.browser.set_page_load_timeout(15)

    # yield context
    # context.close()


def after_all(context):
    print("inside after_all\n")
    context.browser.quit()

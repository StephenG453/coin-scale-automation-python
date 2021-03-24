class HomePage:
    URL = 'http://ec2-54-208-152-154.compute-1.amazonaws.com/'

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)


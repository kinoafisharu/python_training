from selenium.webdriver.firefox.webdriver import WebDriver
from fixtures.session import SessionHelper
from fixtures.object import ObjectHelper


class Application:
    def __init__(self):
        self.wd = WebDriver(
            capabilities={"marionette": False},
            firefox_binary="/home/asteroid/programms/firefox/firefox",
        )
        self.session = SessionHelper(self)
        self.object = ObjectHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()

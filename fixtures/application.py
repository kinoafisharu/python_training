from selenium.webdriver.firefox.webdriver import WebDriver
from fixtures.session import SessionHelper
from fixtures.object import ObjectHelper

class Application:


    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False}, firefox_binary="/home/asteroid/programms/firefox/firefox")
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.object = ObjectHelper(self)

    def open_group_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")

    def open_person_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

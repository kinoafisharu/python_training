# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from models import *

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_for_addressbook(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False}, firefox_binary="/home/asteroid/programms/firefox/firefox")
        self.wd.implicitly_wait(60)

    # def test_add_group(self):
    #     wd = self.wd
    #     self.open_home_page(wd)
    #     self.login(wd, username="admin", password="secret")
    #     self.create_group_form(wd, Group(name="test progon", header="jhvgvhgv", footer="khgcvkvv"))
    #     self.return_to_group_page(wd)
    #     self.logout(wd)
    #
    # def test_add_empty_group(self):
    #     wd = self.wd
    #     self.open_home_page(wd)
    #     self.login(wd, username="admin", password="secret")
    #     self.create_group_form(wd, Group(name="", header="", footer=""))
    #     self.return_to_group_page(wd)
    #     self.logout(wd)

    def test_add_person(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.create_person_form(wd, Person(name="1", lastname="2", address="3", mobile="4", email="5"))
        self.logout(wd)

    def create_person_form(self, wd, person):
        # init_person_creation
        wd.find_element_by_link_text("add new").click()
        # fill_person_form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(person.name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(person.lastname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(person.address)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(person.mobile)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(person.email)
        # submit_person_creation
        wd.find_element_by_name("submit").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_group_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def create_group_form(self, wd, group):
        # init_group_creation
        wd.find_element_by_name("new").click()
        # fill_group_form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit_group_creation
        wd.find_element_by_name("submit").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/group.php")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()

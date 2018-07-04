from models.models import Group
from models.models import Person
import re


class ObjectHelper:
    # main methods
    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    # group methods
    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.get("http://localhost/addressbook/group.php")

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create_group_form(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init_group_creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit_group_creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()
        self.group_cache = None

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        # submin deletion
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None

    def edit_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        # submit edit
        wd.find_element_by_name("edit").click()
        # fill_first_group
        self.fill_group_form(new_group_data)
        # submit_group_update
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None

    def edit_group_form(self, group):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # submit edit
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        # submit_group_update
        wd.find_element_by_name("update").click()
        self.return_to_group_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def edit_first_group(self, new_group_data):
        self.edit_group_by_index(0, new_group_data)

    def count_group(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)


    # person methods
    def open_person_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("selected[]")) > 0):
            wd.get("http://localhost/addressbook/index.php")

    def create_person_form(self, person):
        wd = self.app.wd
        self.open_group_page()
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
        self.person_cache = None

    def delete_first_person(self):
        self.delete_person_by_index(0)

    def delete_person_by_index(self, index):
        wd = self.app.wd
        self.open_person_page()
        # select first person
        wd.find_element_by_name("selected[]").click()
        # submin deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.person_cache = None

    def select_person_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr/td[7]/a/img")[index].click()

    def count_person(self):
        wd = self.app.wd
        self.open_person_page()
        return len(wd.find_elements_by_name("selected[]"))

    def edit_person_form(self, person):
        self.edit_person_form_by_index(0)

    def edit_person_form_by_index(self, index, person):
        wd = self.app.wd
        self.open_person_page()
        # init_person_edit
        self.select_person_by_index(index)
        wd.find_element_by_name("modifiy").click()
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
        # submit_person_update
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        wd.find_element_by_xpath("//div").click()
        self.person_cache = None

    person_cache = None

    def get_person_list(self):
        if self.person_cache is None:
            wd = self.app.wd
            self.open_person_page()
            self.person_cache = []
            for row in wd.find_elements_by_name("entry"):
                elements = row.find_elements_by_tag_name("td")
                id = elements[0].find_element_by_tag_name("input").get_attribute("value")
                lastname = elements[1].text
                firstname = elements[2].text
                all_phones = elements[5].text
                self.person_cache.append(Person(
                                                name=firstname,
                                                lastname=lastname,
                                                id=id,
                                                all_phones_frome_home_page=all_phones,
                                                )
                                         )
        return list(self.person_cache)

    def open_person_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_person_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_person_view_by_index(self, index):
        wd = self.app.wd
        self.open_person_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_person_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_person_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        secondphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Person(name=firstname,
                        lastname=lastname,
                        id=id,
                        mobile=mobile,
                        homephone=homephone,
                        workphone=workphone,
                        secondphone=secondphone,
                        )


    def get_person_from_view_page(self, index):
        wd = self.app.wd
        self.open_person_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        secondphone = re.search("P: (.*)", text).group(1)
        return Person(mobile=mobile,
                      homephone=homephone,
                      workphone=workphone,
                      secondphone=secondphone,
                      )

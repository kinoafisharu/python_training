from models.models import Group
from models.models import Person


class ObjectHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.get("http://localhost/addressbook/group.php")

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

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # submin deletion
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None

    def delete_first_person(self):
        wd = self.app.wd
        self.open_person_page()
        # select first person
        wd.find_element_by_name("selected[]").click()
        # submin deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.person_cache = None

    def edit_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
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

    def count_group(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    def count_person(self):
        wd = self.app.wd
        self.open_person_page()
        return len(wd.find_elements_by_name("selected[]"))

    def edit_person_form(self, person):
        wd = self.app.wd
        self.open_person_page()
        # init_person_edit
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[7]/a/img").click()
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
                self.person_cache.append(Person(name=firstname, lastname=lastname, id=id))
        return list(self.person_cache)

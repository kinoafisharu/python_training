# -*- coding: utf-8 -*-
import pytest
from models import *
from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
        app.login(username="admin", password="secret")
        app.create_group_form(Group(name="test progon", header="jhvgvhgv", footer="khgcvkvv"))
        app.logout()

def test_add_empty_group(app):
        app.login(username="admin", password="secret")
        app.create_group_form(Group(name="", header="", footer=""))
        app.logout()

def test_add_person(app):
        app.login(username="admin", password="secret")
        app.create_person_form(Person(name="1", lastname="2", address="3", mobile="4", email="5"))
        app.logout()


if __name__ == '__main__':
    unittest.main()

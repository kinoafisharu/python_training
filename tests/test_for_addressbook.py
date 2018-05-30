# -*- coding: utf-8 -*-
import pytest
from fixtures.application import Application
from models.models import *


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
        app.session.login(username="admin", password="secret")
        app.object.create_group_form(Group(name="test progon", header="jhvgvhgv", footer="khgcvkvv"))
        app.session.logout()

def test_add_empty_group(app):
        app.session.login(username="admin", password="secret")
        app.object.create_group_form(Group(name="", header="", footer=""))
        app.session.logout()

def test_add_person(app):
        app.session.login(username="admin", password="secret")
        app.object.create_person_form(Person(name="1", lastname="2", address="3", mobile="4", email="5"))
        app.session.logout()


if __name__ == '__main__':
    unittest.main()

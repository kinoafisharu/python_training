# -*- coding: utf-8 -*-
from models.models import Group, Person


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.object.edit_group_form(Group(name="new test progon", header="new jhvgvhgv", footer="new khgcvkvv"))
    app.session.logout()


def test_edit_person(app):
    app.session.login(username="admin", password="secret")
    app.object.edit_person_form(Person(name="new 1", lastname="new 2", address="new 3", mobile="new 4", email="new 5"))
    app.session.logout()
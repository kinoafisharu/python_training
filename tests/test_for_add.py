# coding: utf-8

from models.models import Group, Person


def test_add_group(app):
    app.object.create_group_form(Group(name="test progon",
                                       header="jhvgvhgv",
                                       footer="khgcvkvv",
                                       )
                                 )

def test_add_empty_group(app):
    app.object.create_group_form(Group(name="",
                                       header="",
                                       footer="",
                                       )
                                 )

def test_add_person(app):
    app.object.create_person_form(Person(name="1",
                                         lastname="2",
                                         address="3",
                                         mobile="4",
                                         email="5",
                                         )
                                  )


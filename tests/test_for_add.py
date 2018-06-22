# coding: utf-8

from models.models import Group, Person


def test_add_group(app):
    old_groups = app.object.get_group_list()
    app.object.create_group_form(Group(name="test progon",
                                       header="jhvgvhgv",
                                       footer="khgcvkvv",
                                       )
                                 )
    new_groups = app.object.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(app):
    old_groups = app.object.get_group_list()
    app.object.create_group_form(Group(name="",
                                       header="",
                                       footer="",
                                       )
                                 )
    new_groups = app.object.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_add_person(app):
    app.object.create_person_form(Person(name="1",
                                         lastname="2",
                                         address="3",
                                         mobile="4",
                                         email="5",
                                         )
                                  )


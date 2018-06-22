# coding: utf-8

from models.models import Group
from models.models import Person



def test_edit_group_name(app):
    if app.object.count_group() == 0:
        app.object.create_group_form(Group(name="test"))
    old_groups = app.object.get_group_list()
    app.object.edit_first_group(Group(name="new test progon",
                                     )
                               )
    new_groups = app.object.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_group_header(app):
    if app.object.count_group() == 0:
        app.object.create_group_form(Group(name="test"))
    old_groups = app.object.get_group_list()
    app.object.edit_first_group(Group(header="new header",
                                     )
                               )
    new_groups = app.object.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_person(app):
    if app.object.count_person() == 0:
        app.object.create_person_form(Person(name="test",
                                             lastname="test",
                                             address="test",
                                             email="test",
                                             mobile="test",
                                             )
                                      )
    app.object.edit_person_form(Person(name="new 1",
                                       lastname="new 2",
                                       address="new 3",
                                       mobile="new 4",
                                       email="new 5",
                                       )
                                )

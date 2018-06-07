# coding: utf-8

from models.models import Group
from models.models import Person



def test_edit_group_name(app):
    app.object.edit_first_group(Group(name="new test progon",
                                     )
                               )


def test_edit_group_header(app):
    app.object.edit_first_group(Group(header="new header",
                                     )
                               )


def test_edit_person(app):
    app.object.edit_person_form(Person(name="new 1",
                                       lastname="new 2",
                                       address="new 3",
                                       mobile="new 4",
                                       email="new 5",
                                       )
                                )

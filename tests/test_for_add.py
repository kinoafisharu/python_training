# coding: utf-8

from models.models import Group
from models.models import Person


def test_add_group(app):
    old_groups = app.object.get_group_list()
    group = Group(name="test progon",
                  header="jhvgvhgv",
                  footer="khgcvkvv",
                  )
    app.object.create_group_form(group)
    new_groups = app.object.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_empty_group(app):
    old_groups = app.object.get_group_list()
    group = Group(name="",
                  header="",
                  footer="",
                  )
    app.object.create_group_form(group)
    new_groups = app.object.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_person(app):
    old_persons = app.object.get_person_list()
    person = Person(name="1",
                    lastname="2",
                    address="3",
                    mobile="4",
                    email="5",
                    )
    app.object.create_person_form(person)
    new_persons = app.object.get_person_list()
    assert len(old_persons) + 1 == len(new_persons)
    old_persons.append(person)
    assert sorted(old_persons, key=Person.id_or_max) == sorted(new_persons, key=Person.id_or_max)


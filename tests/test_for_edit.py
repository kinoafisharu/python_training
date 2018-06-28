# coding: utf-8

from models.models import Group
from models.models import Person
from random import randrange


def test_edit_group_name(app):
    if app.object.count_group() == 0:
        app.object.create_group_form(Group(name="test"))
    old_groups = app.object.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="new test progon")
    group.id = old_groups[index].id
    app.object.edit_group_by_index(index, group)
    new_groups = app.object.get_group_list()
    assert len(old_groups) == app.object.count_group()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_group_header(app):
    if app.object.count_group() == 0:
        app.object.create_group_form(Group(name="test"))
    old_groups = app.object.get_group_list()
    app.object.edit_first_group(Group(header="new header",
                                     )
                               )
    new_groups = app.object.get_group_list()
    assert len(old_groups) == app.object.count_group()


def test_edit_person(app):
    if app.object.count_person() == 0:
        app.object.create_person_form(Person(name="test",
                                             lastname="test",
                                             address="test",
                                             email="test",
                                             mobile="test",
                                             )
                                      )
    old_persons = app.object.get_person_list()
    index = randrange(len(old_persons))
    person = Person(name="new 1",
                    lastname="new 2",
                    address="new 3",
                    mobile="new 4",
                    email="new 5",
                    )
    person.id = old_persons[index].id
    app.object.edit_person_form_by_index(index, person)
    new_persons = app.object.get_person_list()
    assert len(old_persons) == app.object.count_person()
    old_persons[index] = person
    assert sorted(old_persons, key=Person.id_or_max) == sorted(new_persons, key=Person.id_or_max)

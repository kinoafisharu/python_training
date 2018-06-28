from models.models import Group
from models.models import Person
from random import randrange


def test_delete_some_group(app):
    if app.object.count_group() == 0:
        app.object.create_group_form(Group(name="test"))
    old_groups = app.object.get_group_list()
    index = randrange(len(old_groups))
    app.object.delete_group_by_index(index)
    new_groups = app.object.get_group_list()
    assert len(old_groups) - 1 == app.object.count_group()
    old_groups[index:index+1] = []
    assert old_groups == new_groups


def test_delete_some_person(app):
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
    app.object.delete_person_by_index(index)
    new_persons = app.object.get_person_list()
    assert len(old_persons) - 1 == app.object.count_person()
    # old_persons[index:index+1] = []
    # assert old_persons == new_persons

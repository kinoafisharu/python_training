from models.models import Group
from models.models import Person


def test_delete_first_group(app):
    if app.object.count_group() == 0:
        app.object.create_group_form(Group(name="test"))
    old_groups = app.object.get_group_list()
    app.object.delete_first_group()
    new_groups = app.object.get_group_list()
    assert len(old_groups) - 1 == app.object.count_group()
    old_groups[0:1] = []
    assert old_groups == new_groups


def test_delete_first_person(app):
    if app.object.count_person() == 0:
        app.object.create_person_form(Person(name="test",
                                             lastname="test",
                                             address="test",
                                             email="test",
                                             mobile="test",
                                             )
                                      )
    old_persons = app.object.get_person_list()
    app.object.delete_first_person()
    new_persons = app.object.get_person_list()
    assert len(old_persons) - 1 == app.object.count_person()
    old_persons[0:1] = []
    assert old_persons == new_persons

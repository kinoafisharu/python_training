from models.models import Group, Person


def test_delete_first_group(app):
    if app.object.count_group() == 0:
        app.object.create_group_form(Group(name="test"))
    app.object.delete_first_group()


#def test_delete_first_person(app):
#    app.object.delete_first_person()


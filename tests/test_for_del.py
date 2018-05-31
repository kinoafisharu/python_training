
def test_delete_first_group(app):

    app.session.login(username="admin", password="secret")
    app.object.delete_first_group()
    app.session.logout()


def test_delete_first_person(app):

    app.session.login(username="admin", password="secret")
    app.object.delete_first_person()
    app.session.logout()
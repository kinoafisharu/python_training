import re


def test_phones_on_home_page(app):
    person_from_home_page = app.object.get_person_list()[0]
    person_from_edit_page = app.object.get_person_info_from_edit_page(0)
    assert person_from_home_page.homephone == clear(person_from_edit_page.homephone)
    assert person_from_home_page.workphone == clear(person_from_edit_page.workphone)
    assert person_from_home_page.mobile == clear(person_from_edit_page.mobile)
    assert person_from_home_page.secondphone == clear(person_from_edit_page.secondphone)


def test_phones_on_person_view_page(app):
    person_from_view_page = app.object.get_person_from_view_page(0)
    person_from_edit_page = app.object.get_person_info_from_edit_page(0)
    assert person_from_view_page.homephone == person_from_edit_page.homephone
    assert person_from_view_page.workphone == person_from_edit_page.workphone
    assert person_from_view_page.mobile == person_from_edit_page.mobile
    assert person_from_view_page.secondphone == person_from_edit_page.secondphone

def clear(str):
    return re.sub("[() -]", "", str)
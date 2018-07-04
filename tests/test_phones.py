import re


def test_phones_on_home_page(app):
    person_from_home_page = app.object.get_person_list()[0]
    person_from_edit_page = app.object.get_person_info_from_edit_page(0)
    assert person_from_home_page.all_phones_frome_home_page == merge_phones_like_on_home_page(person_from_edit_page)

def test_phones_on_person_view_page(app):
    person_from_view_page = app.object.get_person_from_view_page(0)
    person_from_edit_page = app.object.get_person_info_from_edit_page(0)
    assert person_from_view_page.homephone == person_from_edit_page.homephone
    assert person_from_view_page.workphone == person_from_edit_page.workphone
    assert person_from_view_page.mobile == person_from_edit_page.mobile
    assert person_from_view_page.secondphone == person_from_edit_page.secondphone

def clear(str):
    return re.sub("[() -]", "", str)

def merge_phones_like_on_home_page(person):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [person.homephone,
                                        person.mobile,
                                        person.workphone,
                                        person.secondphone]
                                       )
                                )
                            )
                     )

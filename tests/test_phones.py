import re
from random import randrange


def test_phones_on_home_page(app):
    person_from_home_page = app.object.get_person_list()[0]
    person_from_edit_page = app.object.get_person_info_from_edit_page(0)
    assert person_from_home_page.all_phones_frome_home_page == merge_phones_like_on_home_page(person_from_edit_page)

# def test_phones_on_person_view_page(app):
#     person_from_view_page = app.object.get_person_from_view_page(0)
#     person_from_edit_page = app.object.get_person_info_from_edit_page(0)
#     assert person_from_view_page.all_phones_frome_home_page == merge_phones_like_on_home_page(person_from_edit_page)


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


def merge_emails_like_on_home_page(person):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [person.email,
                                        person.email2,
                                        person.email3,]
                                       )
                                )
                            )
                     )

def test_data_some_person(app):
    if app.object.count_person() == 0:
        app.object.create_person_form(Person(name="test",
                                             lastname="test",
                                             address="test",
                                             email="test",
                                             mobile="12345",
                                             homephone="987654",
                                             workphone="765432",
                                             secondphone="876543"
                                             )
                                      )
    list_persons = app.object.get_person_list()
    index = randrange(len(list_persons))
    person_from_home_page = app.object.get_person_list()[index]
    person_from_edit_page = app.object.get_person_info_from_edit_page(index)
    assert person_from_home_page.all_phones_frome_home_page == merge_phones_like_on_home_page(person_from_edit_page)
    assert person_from_home_page.all_emails_frome_home_page == merge_emails_like_on_home_page(person_from_edit_page)

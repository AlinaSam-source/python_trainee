import re
from random import randrange


def test_contact_info_on_edit_page(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_homepage = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_homepage.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_homepage.firstName == contact_from_edit_page.firstName
    assert contact_from_homepage.lastname == contact_from_edit_page.lastname
    assert contact_from_homepage.address == contact_from_edit_page.address
    assert contact_from_homepage.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def test_phones_on_view_page(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_homepage = app.contact.get_contact_list()[index]
    contact_from_view_page = app.contact.get_contact_info_from_view_page(index)
    assert contact_from_homepage.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_view_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                      [contact.home, contact.mobile,
                                       contact.work, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                      [contact.email, contact.email2,
                                       contact.email3])))



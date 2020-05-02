from model.contact import Contact
from random import randrange


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstName="test"))

    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))

    contact_expected_deleted = app.contact.delete_contact_by_index(index)

    assert len(old_contacts) - 1 == app.contact.count()

    new_contacts = app.contact.get_contact_list()

    contact_actually_deleted = list(set(old_contacts) - set(new_contacts))[0]
    assert contact_expected_deleted == contact_actually_deleted

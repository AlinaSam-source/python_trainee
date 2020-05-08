from model.contact import Contact
from random import randrange


def test_delete_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstName="test"))

    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))

    contact_expected_deleted = app.contact.delete_contact_by_index(index)

    new_contacts = db.get_contact_list()

    contact_actually_deleted = list(set(old_contacts) - set(new_contacts))[0]
    assert contact_expected_deleted == contact_actually_deleted

    if check_ui:
         assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

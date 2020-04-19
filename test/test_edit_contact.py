from model.contact import Contact
from random import randrange

def test_edit_contact_firstName (app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstName="test"))

    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    element_to_edit = sorted(old_contacts, key=Contact.id_or_max)[index]
    old_id = element_to_edit.id
    old_firstname = element_to_edit.firstName

    new_firstname = old_firstname + '-Modified'
    expected_edited_contact = Contact(id=old_id, firstName=new_firstname)
    app.contact.edit_contact_by_id(expected_edited_contact)

    new_contacts = app.contact.get_contact_list()

    assert len(old_contacts) == len(new_contacts)

    assert sorted(new_contacts, key=Contact.id_or_max)[index].firstName == new_firstname


def test_edit_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstName="test"))

    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    element_to_edit = sorted(old_contacts, key=Contact.id_or_max)[index]
    old_id = element_to_edit.id
    old_lastname = element_to_edit.lastname

    new_lastname = old_lastname + '-Modified'
    expected_edited_contact = Contact(id=old_id, lastname=new_lastname)
    app.contact.edit_contact_by_id(expected_edited_contact)

    new_contacts = app.contact.get_contact_list()

    assert len(old_contacts) == len(new_contacts)

    assert sorted(new_contacts, key=Contact.id_or_max)[index].id == old_id
    assert sorted(new_contacts, key=Contact.id_or_max)[index].lastname == new_lastname
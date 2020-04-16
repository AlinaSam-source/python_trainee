from model.contact import Contact

def test_edit_contact_firstName (app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstName="test"))

    old_contacts = app.contact.get_contact_list()
    element_to_edit = sorted(old_contacts, key=Contact.id_or_max)[0]
    old_id = element_to_edit.id
    old_firstname = element_to_edit.firstName

    new_firstname = old_firstname + '-Modified'
    expected_edited_contact = Contact(id=old_id, firstName=new_firstname)
    app.contact.edit_contact(expected_edited_contact)

    new_contacts = app.contact.get_contact_list()

    assert len(old_contacts) == len(new_contacts)

    assert sorted(new_contacts, key=Contact.id_or_max)[0].firstName == new_firstname


def test_edit_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstName="test"))

    old_contacts = app.contact.get_contact_list()
    element_to_edit = sorted(old_contacts, key=Contact.id_or_max)[0]
    old_id = element_to_edit.id
    old_lastname = element_to_edit.lastname

    new_lastname = old_lastname + '-Modified'
    expected_edited_contact = Contact(id=old_id, lastname=new_lastname)
    app.contact.edit_contact(expected_edited_contact)

    new_contacts = app.contact.get_contact_list()

    assert len(old_contacts) == len(new_contacts)

    assert sorted(new_contacts, key=Contact.id_or_max)[0].id == old_id
    assert sorted(new_contacts, key=Contact.id_or_max)[0].lastname == new_lastname
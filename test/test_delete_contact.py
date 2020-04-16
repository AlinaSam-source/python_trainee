from model.contact import Contact


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstName="test"))
    old_contacts = app.contact.get_contact_list()
    contact_expected_deleted = app.contact.delete()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    contact_actually_deleted = list(set(old_contacts) - set(new_contacts))[0]
    assert contact_expected_deleted == contact_actually_deleted


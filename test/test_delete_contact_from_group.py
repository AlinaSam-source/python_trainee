from random import randrange
from model.group import Group
from fixture.orm import ORMFixure
from fixture.contact import Contact

def test_add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstName="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))

    db = ORMFixure(host='127.0.0.1', name='addressbook', user='root', password='')

    groups = db.get_group_list()
    index_group = randrange(len(groups))
    group_delete_contact_from = sorted(groups, key=Group.id_or_max)[index_group]
    group_id = group_delete_contact_from.id

    contacts = app.contact.get_contact_list()
    index_contact = randrange(len(contacts))
    contact = sorted(contacts, key=Contact.id_or_max)[index_contact]
    contact_id_expected_to_delete = contact.id

    app.contact.add_contact_to_group(contact_id_expected_to_delete, group_id)

    old_contacts_not_in_group = db.get_contacts_not_in_group(Group(id='%s' % group_id))
    app.contact.delete_contact_from_group(contact_id_expected_to_delete, group_id)
    new_contacts_not_in_group = db.get_contacts_not_in_group(Group(id='%s' % group_id))

    contact_actually_deleted_from_group = list(set(new_contacts_not_in_group) - set(old_contacts_not_in_group))[0]
    contact_id_of_deleted_contact = contact_actually_deleted_from_group.id

    assert contact_id_of_deleted_contact == contact_id_expected_to_delete
    assert contact_actually_deleted_from_group == contact






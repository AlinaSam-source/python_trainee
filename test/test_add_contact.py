# -*- coding: utf-8 -*-
import pytest

from model.contact import Contact


def test_add_new_contact(app, json_contacts, db, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)

    new_contacts = db.get_contact_list()

    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    if check_ui:
         assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

#def test_add_empty_contact(app):
    #old_contacts = app.contact.get_contact_list()
    #app.contact.create(Contact(firstName="", middlename="", lastname="", nickname="", title="", company="", address="", home="", mobile="",
                               #work="", fax="", email="", email2="", email3="", homepage="", bday="-", bmonth="-", byear="", aday="-", amonth="-",
                               #ayear="", address2="", phone2="", notes=""))
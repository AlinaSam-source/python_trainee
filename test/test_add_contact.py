# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstName="877", middlename="877", lastname="877", nickname="Alina", title="Alina", company="Infopulse", address="Polyova str 24D", home="123", mobile="123",
                               work="123", fax="123", email="1234", email2="1234", email3="1234", homepage="1234", bday="18", bmonth="September", byear="1996", aday="18", amonth="August",
                               ayear="1996", address2="1", phone2="1", notes="1")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_add_empty_contact(app):
    #old_contacts = app.contact.get_contact_list()
    #app.contact.create(Contact(firstName="", middlename="", lastname="", nickname="", title="", company="", address="", home="", mobile="",
                               #work="", fax="", email="", email2="", email3="", homepage="", bday="-", bmonth="-", byear="", aday="-", amonth="-",
                               #ayear="", address2="", phone2="", notes=""))
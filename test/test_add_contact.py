# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "". join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_days():
    return str(random.randint(1, 31))


def random_year():
    return str(random.randint(1000, 9999))


def random_month():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    return str(random.choice(months))


testdata = [Contact(firstName=random_string("firstName", 10), middlename=random_string("middlename", 20),
                    lastname=random_string("lastname", 10), nickname=random_string("nickname", 10), title=random_string("title", 10),
                    company=random_string("company", 10), address=random_string("address", 10), home=random_string("home", 10),
                    mobile=random_string("mobile", 10), work=random_string("work", 10), fax=random_string("fax", 10),
                    email=random_string("email", 10), email2=random_string("email2", 10), email3=random_string("email3", 10),
                    homepage=random_string("homepage", 10), bday=random_days(), bmonth=random_month(),
                    byear=random_year(), amonth=random_month(), aday=random_days(),
                    ayear=random_year(), address2=random_string("address2", 10), phone2=random_string("phone2", 10),
                    notes=random_string("notes", 10)
) for i in range(5)]



@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)

    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()

    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_add_empty_contact(app):
    #old_contacts = app.contact.get_contact_list()
    #app.contact.create(Contact(firstName="", middlename="", lastname="", nickname="", title="", company="", address="", home="", mobile="",
                               #work="", fax="", email="", email2="", email3="", homepage="", bday="-", bmonth="-", byear="", aday="-", amonth="-",
                               #ayear="", address2="", phone2="", notes=""))
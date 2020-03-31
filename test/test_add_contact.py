# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_new_contact(app):
    app.pages.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstName="Alina", middlename="Alina", lastname="Alina", nickname="Alina", title="Alina", company="Infopulse", address="Polyova str 24D", home="123", mobile="123",
                               work="123", fax="123", email="1234", email2="1234", email3="1234", homepage="1234", bday="18", bmonth="September", byear="1996", aday="18", amonth="August",
                               ayear="1996", address2="1", phone2="1", notes="1"))
    app.session.logout()


def test_add_empty_contact(app):
    app.pages.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstName="", middlename="", lastname="", nickname="", title="", company="", address="", home="", mobile="",
                               work="", fax="", email="", email2="", email3="", homepage="", bday="-", bmonth="-", byear="", aday="-", amonth="-",
                               ayear="", address2="", phone2="", notes=""))
    app.session.logout()
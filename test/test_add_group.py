# -*- coding: utf-8 -*-
from model.group import Group

def test_add_new_group (app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="a", header="a", footer="a"))
    app.session.logout()

def test_add_new_empty_group (app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

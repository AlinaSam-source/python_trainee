# -*- coding: utf-8 -*-
from model.group import Group

def test_add_new_group (app):
    app.group.create(Group(name="a", header="a", footer="a"))


def test_add_new_empty_group (app):
    app.group.create(Group(name="", header="", footer=""))

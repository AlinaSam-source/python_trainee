# -*- coding: utf-8 -*-
from model.group import Group
import pytest

def test_add_new_group(app, db, json_groups, check_ui):
    group = json_groups
    with pytest.allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with pytest.allure.step('Add a group %s to the list' % group):
        app.group.create(group)
    with pytest.allure.step('New group list is equal to tte old list with added group'):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

# def test_add_new_empty_group (app):
# old_groups = app.group.get_group_list()
# group = Group(name="", header="", footer="")
# app.group.create(group)
# new_groups = app.group.get_group_list()
# assert len(old_groups) + 1 == app.group.count()
# old_groups.append(group)
# assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

from model.group import Group
from random import randrange


def test_delete_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))

    group_expected_deleted = app.group.delete_group_by_index(index)
    new_groups = db.get_group_list()

    group_actually_deleted = list(set(old_groups) - set(new_groups))[0]
    assert group_expected_deleted == group_actually_deleted

    if check_ui:
         assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
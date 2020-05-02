from model.group import Group
from random import randrange


def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))

    group_expected_deleted = app.group.delete_group_by_index(index)

    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()

    group_actually_deleted = list(set(old_groups) - set(new_groups))[0]
    assert group_expected_deleted == group_actually_deleted

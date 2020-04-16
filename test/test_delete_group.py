from model.group import Group

def test_delete_group (app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    group_expected_deleted = app.group.delete()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    group_actually_deleted = list(set(old_groups) - set(new_groups))[0]
    assert group_expected_deleted == group_actually_deleted

from model.group import Group
from random import randrange


def test_edit_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))

    old_groups = db.get_group_list()
    index = randrange(len(old_groups))

    group_to_edit = sorted(old_groups, key=Group.id_or_max)[index]
    old_id = group_to_edit.id
    old_name = group_to_edit.name

    new_name = old_name + '-Modified'
    group_data_to_edit = Group(id=old_id, name=new_name)
    app.group.edit_group_by_id(group_data_to_edit)

    new_groups = db.get_group_list()

    assert sorted(new_groups, key=Group.id_or_max)[index].name == new_name

    if check_ui:
         assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

#def test_edit_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    old_groups = app.group.get_group_list()
#    app.group.edit_group(Group(header='Alina'))
#    new_groups = app.group.get_group_list()
#   assert len(old_groups) == len(new_groups)

from model.group import Group
from random import randrange


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))

    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))

    group_to_edit = sorted(old_groups, key=Group.id_or_max)[index]
    old_id = group_to_edit.id
    old_name = group_to_edit.name

    new_name = old_name + '-Modified'
    group_data_to_edit = Group(id=old_id, name=new_name)
    app.group.edit_group_by_id(group_data_to_edit)

    assert len(old_groups) == app.group.count()

    new_groups = app.group.get_group_list()

    assert sorted(new_groups, key=Group.id_or_max)[index].name == new_name

#def test_edit_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    old_groups = app.group.get_group_list()
#    app.group.edit_group(Group(header='Alina'))
#    new_groups = app.group.get_group_list()
#   assert len(old_groups) == len(new_groups)

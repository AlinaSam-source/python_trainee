from model.group import Group

def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))

    old_groups = app.group.get_group_list()
    group_to_edit = sorted(old_groups, key=Group.id_or_max)[0]
    old_id = group_to_edit.id
    old_name = group_to_edit.name

    new_name = old_name + '-Modified'
    group_data_to_edit = Group(id=old_id, name=new_name)
    app.group.edit_group(group_data_to_edit)

    new_groups = app.group.get_group_list()

    assert len(old_groups) == len(new_groups)

    assert sorted(new_groups, key=Group.id_or_max)[0].name == new_name

#def test_edit_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    old_groups = app.group.get_group_list()
#    app.group.edit_group(Group(header='Alina'))
#    new_groups = app.group.get_group_list()
#   assert len(old_groups) == len(new_groups)

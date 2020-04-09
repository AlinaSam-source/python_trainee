from model.group import Group

def test_edit_group_name(app):
    app.group.edit_group(Group(name='Alina'))


def test_edit_group_header(app):
    app.group.edit_group(Group(header='Alina'))

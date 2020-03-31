from model.edit import Edit

def test_edit_group(app):
    app.pages.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.edit_group(Edit(field="group_name", name="Group"))
    app.session.logout()
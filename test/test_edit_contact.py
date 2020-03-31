from model.edit import Edit

def test_edit_contact (app):
    app.pages.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.edit_contact(Edit(field="middlename", name="Alina"))
    app.session.logout()
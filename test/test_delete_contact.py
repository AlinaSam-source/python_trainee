def test_delete_contact(app):
    app.pages.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.delete()
    app.session.logout()
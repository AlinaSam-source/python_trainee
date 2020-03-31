def test_delete_group (app):
    app.pages.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.delete()
    app.session.logout()
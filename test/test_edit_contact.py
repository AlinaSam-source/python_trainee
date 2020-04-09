from model.contact import Contact

def test_edit_contact_firstName (app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstName="test"))
    app.contact.edit_contact(Contact(firstName="Sveta"))


def test_edit_contact_middleName (app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstName="test"))
    app.contact.edit_contact(Contact(middlename="Sveta"))
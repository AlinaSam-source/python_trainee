from model.contact import Contact

def test_edit_contact_firstName (app):
    app.contact.edit_contact(Contact(firstName="Sveta"))


def test_edit_contact_middleName (app):
    app.contact.edit_contact(Contact(middlename="Sveta"))
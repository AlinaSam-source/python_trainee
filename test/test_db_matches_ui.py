from model.group import Group
from model.contact import Contact

def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    db_list = db.get_group_list()
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_contact_list(app, db):
    name = app.contact.get_contact_list_field('firstName')
    lastname = app.contact.get_contact_list_field('lastname')
    name_db = db.get_contact_list_field('firstName')
    lastname_db = db.get_contact_list_field('lastname')
    phones_db = db.get_contact_list_field('phones')
    phones = app.contact.get_contact_list_field('all_phones_from_home_page')
    phones_db_merged = merge_phones_like_on_home_page(phones_db)
    emails_db = db.get_contact_list_field('emails')
    emails = app.contact.get_contact_list_field('all_emails_from_home_page')
    emails_db_merged = merge_emails_like_on_home_page(emails_db)
    address = app.contact.get_contact_list_field('address')
    address_db = db.get_contact_list_field('address')
    assert sorted(emails, key=Contact.id_or_max) == sorted(emails_db_merged, key=Contact.id_or_max)
    assert sorted(phones, key=Contact.id_or_max) == sorted(phones_db_merged, key=Contact.id_or_max)
    assert sorted(name_db, key=Contact.id_or_max) == sorted(name, key=Contact.id_or_max)
    assert sorted(lastname_db, key=Contact.id_or_max) == sorted(lastname, key=Contact.id_or_max)
    assert sorted(address, key=Contact.id_or_max) == sorted(address_db, key=Contact.id_or_max)



def merge_phones_like_on_home_page(phones_db):
    list=[]
    for element in phones_db:
        phones = "\n".join(filter(lambda x: x is not None,
                                      [element.home, element.mobile,
                                       element.work, element.phone2]))
        list.append(Contact(all_phones_from_db=phones))
    return list


def merge_emails_like_on_home_page(emails_db):
    list=[]
    for element in emails_db:
        emails = "\n".join(filter(lambda x: x is not None,
                                      [element.email, element.email2,
                                       element.email3]))
        list.append(Contact(all_emails_from_db=emails))
    return list




from datetime import datetime
from pony.orm import*
from model.group import Group
from model.contact import Contact



class ORMFixure:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixure.ORMContact, table='address_in_groups', column='id', reverse='groups', lazy=True)


    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        home = Optional(str, column='home')
        mobile = Optional(str, column='mobile')
        work = Optional(str, column='work')
        email = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        address = Optional(str, column='address')
        phone2 = Optional(str, column='phone2')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixure.ORMGroup, table='address_in_groups', column='group_id', reverse='contacts', lazy=True)


    def __init__(self, host, name, user, password):
        try:
          self.db.bind('mysql', host=host, database=name, user=user, password=password)
        except BindingError:
            return
        self.db.generate_mapping()
        sql_debug(True)


    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))


    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixure.ORMGroup))


    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstName=contact.firstname, lastname=contact.lastname, home=contact.home, mobile=contact.mobile, work=contact.work, email=contact.email, email2=contact.email2, email3=contact.email3, address=contact.address, phone2=contact.phone2)
        return list(map(convert, contacts))


    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixure.ORMContact if c.deprecated is None))


    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixure.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixure.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(
            select(c for c in ORMFixure.ORMContact if c.deprecated is None and orm_group not in c.groups))

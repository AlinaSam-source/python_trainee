import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)


    def get_group_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for raw in cursor:
                (id, name, header, footer) = raw
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list


    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, home, mobile, work, email, email2, email3, address from addressbook where deprecated='NULL'")
            for raw in cursor:
                (id, firstname, middlename, lastname, home, mobile, work, email, email2, email3, address) = raw
                list.append(Contact(id=str(id), firstName=firstname, lastname=lastname, home=home, mobile=mobile, work=work, email=email, email2=email2, email3=email3, address=address))
        finally:
            cursor.close()
        return list


    def get_contact_list_field(self, field):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, firstname, middlename, lastname, home, mobile, work, email, email2, email3, address, phone2 from addressbook where deprecated='NULL'")
            for raw in cursor:
                (id, firstname, middlename, lastname, home, mobile, work, email, email2, email3, address, phone2) = raw
                if field == 'firstName':
                    list.append(Contact(id=str(id), firstName=firstname))
                if field == 'lastname':
                    list.append(Contact(id=str(id), lastname=lastname))
                if field == 'phones':
                    list.append(Contact(id=str(id), home=home, mobile=mobile, work=work, phone2=phone2))
                if field == 'emails':
                    list.append(Contact(id=str(id), email=email, email2=email2, email3=email3))
                if field == 'address':
                    list.append(Contact(id=str(id), address=address))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
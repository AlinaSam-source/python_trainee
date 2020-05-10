import pymysql.cursors
from fixture.orm import ORMFixure
from model.group import Group

db = ORMFixure(host='127.0.0.1', name='addressbook', user='root', password='')

try:
   l = db.get_contacts_in_group(Group(id='549'))
   for item in l:
       print(item)
   print(len(l))
finally:
    pass





from model.contact import Contact


testdata = [
    Contact(firstName="firstName1", middlename="middlename1",
                    lastname="lastname1", nickname="nickname1", title="title1",
                    company="company1", address="address1", home="home1",
                    mobile="mobile1", work="work1", fax="fax1",
                    email="email1", email2="email21", email3="email31",
                    homepage="homepage1", bday='18', bmonth='August',
                    byear='1996', amonth='August', aday='18',
                    ayear='1996', address2="address21", phone2="phone21",
                    notes="notes1"),
    Contact(firstName="firstName2", middlename="middlename2",
                    lastname="lastname2", nickname="nickname2", title="title2",
                    company="company2", address="address2", home="home2",
                    mobile="mobile2", work="work2", fax="fax2",
                    email="email2", email2="email22", email3="email32",
                    homepage="homepage2", bday='18', bmonth='August',
                    byear='1996', amonth='August', aday='18',
                    ayear='1996', address2="address22", phone2="phone22",
                    notes="notes2")
]



# def random_string(prefix, maxlen):
#     symbols = string.ascii_letters + string.digits
#     return prefix + "". join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
#
# def random_days():
#     return str(random.randint(1, 31))
#
#
# def random_year():
#     return str(random.randint(1000, 9999))
#
#
# def random_month():
#     months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
#               "November", "December"]
#     return str(random.choice(months))
#
#
# testdata = [Contact(firstName=random_string("firstName", 10), middlename=random_string("middlename", 20),
#                     lastname=random_string("lastname", 10), nickname=random_string("nickname", 10), title=random_string("title", 10),
#                     company=random_string("company", 10), address=random_string("address", 10), home=random_string("home", 10),
#                     mobile=random_string("mobile", 10), work=random_string("work", 10), fax=random_string("fax", 10),
#                     email=random_string("email", 10), email2=random_string("email2", 10), email3=random_string("email3", 10),
#                     homepage=random_string("homepage", 10), bday=random_days(), bmonth=random_month(),
#                     byear=random_year(), amonth=random_month(), aday=random_days(),
#                     ayear=random_year(), address2=random_string("address2", 10), phone2=random_string("phone2", 10),
#                     notes=random_string("notes", 10)
# ) for i in range(5)]



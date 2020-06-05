from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re

class ContactHelper:
    def __init__(self, app):
        self.accept_next_alert = True
        self.app = app


    def go_to_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("firstname")) > 0):
            wd.find_element_by_link_text("home").click()


    def return_to_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("firstname")) > 0):
            wd.find_element_by_link_text("home page").click()


    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_contacts_page()
        self.contact_cache = None


    def fill_contact_form(self, contact):
        self.change_field_value("firstname",contact.firstName)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.select_field_value("bday", contact.bday)
        self.select_field_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.select_field_value("aday", contact.aday)
        self.select_field_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.email3)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def select_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)


    def delete_contact_by_index(self, index):
        wd = self.app.wd
        app = self.app
        self.go_to_contacts_page()

        element_to_delete = self.select_contact_by_index(index)
        contact_to_delete = self.resolve_contact(element_to_delete)
        element_to_delete.find_element_by_name("selected[]").click()

        wd.find_element_by_xpath("//input[@value='Delete']").click()
        app.confirmations.assertRegexpMatches(app.confirmations.close_alert_and_get_its_text(), r"^Delete 1 addresses[\s\S]$")

        self.go_to_contacts_page()
        self.contact_cache = None
        return contact_to_delete


    def select_the_first_contact(self):
        wd = self.app.wd
        return wd.find_elements_by_css_selector('#maintable tr:not(:first-child)')[0]


    def select_contact_by_index(self, index):
        wd = self.app.wd
        return wd.find_elements_by_css_selector('#maintable tr:not(:first-child)')[index]


    def select_contact_by_id(self, id):
        wd = self.app.wd
        return wd.find_elements_by_css_selector('#maintable tr:not(:first-child)')[id]


    def open_contact_to_edit_by_index(self, index):
        self.app.open_home_page()
        self.go_to_contacts_page()
        row = self.select_contact_by_index(index)
        cell = row.find_elements_by_tag_name('td')[7]
        cell.find_element_by_tag_name('a').click()


    def open_contact_view_by_index(self, index):
        self.app.open_home_page()
        self.go_to_contacts_page()
        row = self.select_contact_by_index(index)
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()


    def click_edit_the_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_elements_by_css_selector("a[href='edit.php?id=%s']" % id)[0].click()


    def edit_contact_by_id(self, contact):
        wd = self.app.wd
        self.go_to_contacts_page()

        self.click_edit_the_contact_by_id(contact.id)

        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()

        self.return_to_contacts_page()
        self.contact_cache = None


    def count(self):
        wd = self.app.wd
        self.go_to_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))


    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
           wd = self.app.wd
           self.go_to_contacts_page()

           self.contact_cache = []
           for element in wd.find_elements_by_css_selector('#maintable tr:not(:first-child)'):
               self.contact_cache.append(self.resolve_contact(element))

        return list(self.contact_cache)


    def resolve_contact(self, element):
        text_name = element.find_elements_by_css_selector('td:nth-child(3)')[0].text
        text_surname = element.find_elements_by_css_selector('td:nth-child(2)')[0].text
        text_all_phones = element.find_elements_by_css_selector('td:nth-child(6)')[0].text
        text_address = element.find_elements_by_css_selector('td:nth-child(4)')[0].text
        id = element.find_element_by_name("selected[]").get_attribute("value")
        all_emails_from_home_page = element.find_elements_by_css_selector('td:nth-child(5)')[0].text
        return Contact(firstName=text_name, lastname=text_surname, id=id, all_phones_from_home_page=text_all_phones,
                       address=text_address, all_emails_from_home_page=all_emails_from_home_page)



    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstName = wd.find_elements_by_name("firstname")[0].get_attribute("value")
        lastname = wd.find_elements_by_name("lastname")[0].get_attribute("value")
        id = wd.find_elements_by_name("id")[0].get_attribute("value")

        home = wd.find_elements_by_name("home")[0].get_attribute("value")
        mobile = wd.find_elements_by_name("mobile")[0].get_attribute("value")
        phone2 = wd.find_elements_by_name("phone2")[0].get_attribute("value")
        work = wd.find_elements_by_name("work")[0].get_attribute("value")

        email = wd.find_elements_by_name("email")[0].get_attribute("value")
        email2 = wd.find_elements_by_name("email2")[0].get_attribute("value")
        email3 = wd.find_elements_by_name("email3")[0].get_attribute("value")

        address = wd.find_elements_by_name("address")[0].get_attribute("value")

        return Contact(firstName=firstName, lastname=lastname, id=id, home=home, mobile=mobile,
                       work=work, phone2=phone2, email=email, email2=email2, email3=email3, address=address)


    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_elements_by_id('content')[0].text
        home = re.search("H:(.*)", text).group(1)
        work = re.search("W:(.*)", text).group(1)
        mobile = re.search("M:(.*)", text).group(1)
        phone2 = re.search("P:(.*)", text).group(1)

        return Contact(home=home, mobile=mobile, work=work, phone2=phone2)


    def select_group_add_contact_to(self, id):
        wd = self.app.wd
        wd.find_element_by_name("to_group")
        wd.find_element_by_xpath("(//option[@value='%s'])[2]" % id).click()


    def select_group_delete_contact_from(self, id):
        wd = self.app.wd
        wd.find_element_by_name("group")
        wd.find_element_by_xpath('//option[@value="%s"]' % id).click()


    def add_contact_to_group(self, contact_id, group_id ):
        wd = self.app.wd
        self.go_to_contacts_page()
        wd.find_elements_by_css_selector('#maintable td:first-child input[value="%s"]' % contact_id)[0].click()
        self.select_group_add_contact_to(group_id)
        wd.find_element_by_name("add").click()


    def delete_contact_from_group(self, contact_id, group_id ):
        wd = self.app.wd
        self.go_to_contacts_page()
        self.select_group_delete_contact_from(group_id)
        wd.find_elements_by_css_selector('#maintable td:first-child input[value="%s"]' % contact_id)[0].click()
        wd.find_element_by_name("remove").click()



    def get_contact_list_field(self, field):
        list_ui = []
        wd = self.app.wd
        self.go_to_contacts_page()
        for element in wd.find_elements_by_css_selector('#maintable tr:not(:first-child)'):
            list_ui.append(self.resolve_contact_field(element, field))
        return list_ui


    def resolve_contact_field(self, element, field):
        text_name = element.find_elements_by_css_selector('td:nth-child(3)')[0].text
        text_surname = element.find_elements_by_css_selector('td:nth-child(2)')[0].text
        text_all_phones = element.find_elements_by_css_selector('td:nth-child(6)')[0].text
        text_address = element.find_elements_by_css_selector('td:nth-child(4)')[0].text
        id = element.find_element_by_name("selected[]").get_attribute("value")
        all_emails_from_home_page = element.find_elements_by_css_selector('td:nth-child(5)')[0].text
        field_name = field
        if field_name == 'firstName':
            return Contact(id=id, firstName=text_name)
        if field_name == 'lastname':
            return Contact(id=id, lastname=text_surname)
        if field_name == 'all_phones_from_home_page':
            return Contact(id=id, all_phones_from_home_page=text_all_phones)
        if field_name == 'all_emails_from_home_page':
            return Contact(id=id, all_emails_from_home_page=all_emails_from_home_page)
        if field_name == 'address':
            return Contact(id=id, address=text_address)







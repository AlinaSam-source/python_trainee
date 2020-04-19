from selenium.webdriver.support.ui import Select
from model.contact import Contact

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
        id = element.find_element_by_name("selected[]").get_attribute("value")
        return Contact(firstName=text_name, lastname=text_surname, id=id)


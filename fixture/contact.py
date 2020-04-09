from selenium.webdriver.support.ui import Select

class ContactHelper:
    def __init__(self, app):
        self.accept_next_alert = True
        self.app = app


    def create(self, contact):
        wd = self.app.wd
        app = self.app
        # init new contact
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        app.pages.open_page(page_name="home page")


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

    def delete(self):
        wd = self.app.wd
        app = self.app
        app.pages.open_page(page_name="home")
        #select the first contact
        wd.find_element_by_name("selected[]").click()
        # delete the first contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        app.confirmations.assertRegexpMatches(app.confirmations.close_alert_and_get_its_text(), r"^Delete 1 addresses[\s\S]$")
        #go to contacts page
        app.pages.open_page(page_name="home")


    def edit_contact(self, contact):
        wd = self.app.wd
        app = self.app
        app.pages.open_page(page_name="home")
        # select the first contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # edit the name of the first contact
        self.fill_contact_form(contact)
        # confirm the change
        wd.find_element_by_name("update").click()
        # go to contacts page
        app.pages.open_page(page_name="home page")


    def count(self):
        wd = self.app.wd
        app = self.app
        app.pages.open_page(page_name="home")
        return len(wd.find_elements_by_name("selected[]"))


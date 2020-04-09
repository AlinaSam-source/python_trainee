class GroupHelper:
    def __init__(self, app):
        self.app = app


    def create(self, group):
        wd = self.app.wd
        app = self.app
        app.pages.open_page(page_name="groups")
        # group creation
        wd.find_element_by_name("new").click()
        self.fill_group_data(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        app.pages.open_page(page_name="group page")


    def fill_group_data(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def delete(self):
        wd = self.app.wd
        app = self.app
        app.pages.open_page(page_name="groups")
        self.select_the_first_group()
        # delete the first group
        wd.find_element_by_name("delete").click()
        app.pages.open_page(page_name="group page")


    def select_the_first_group(self):
        # select the first group
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()


    def edit_group(self, group_data):
        wd = self.app.wd
        app = self.app
        app.pages.open_page(page_name="groups")
        self.select_the_first_group()
        # edit the name of the first group
        wd.find_element_by_xpath("//input[@name='edit']").click()
        self.fill_group_data(group_data)
        # confirm the change
        wd.find_element_by_name("update").click()
        app.pages.open_page(page_name="group page")

    def count(self):
        wd = self.app.wd
        app = self.app
        app.pages.open_page(page_name="groups")
        return len(wd.find_elements_by_name("selected[]"))
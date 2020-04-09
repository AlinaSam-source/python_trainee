class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()


    def return_groups_list(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()


    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # group creation
        wd.find_element_by_name("new").click()
        self.fill_group_data(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_groups_list()


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
        self.open_groups_page()
        self.select_the_first_group()
        # delete the first group
        wd.find_element_by_name("delete").click()
        self.return_groups_list()


    def select_the_first_group(self):
        # select the first group
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()


    def edit_group(self, group_data):
        wd = self.app.wd
        app = self.app
        self.open_groups_page()
        self.select_the_first_group()
        # edit the name of the first group
        wd.find_element_by_xpath("//input[@name='edit']").click()
        self.fill_group_data(group_data)
        # confirm the change
        wd.find_element_by_name("update").click()
        self.return_groups_list()

    def count(self):
        wd = self.app.wd
        app = self.app
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))
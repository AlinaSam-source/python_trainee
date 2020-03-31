class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        app = self.app
        app.pages.open_page(page_name="groups")
        # group creation
        wd.find_element_by_name("new").click()
        # fill group data
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        app.pages.open_page(page_name="group page")


    def delete(self):
        wd = self.app.wd
        app = self.app
        app.pages.open_page(page_name="groups")
        # select the first group
        wd.find_element_by_name("selected[]").click()
        # delete the first group
        wd.find_element_by_name("delete").click()
        app.pages.open_page(page_name="group page")

    def edit_group(self, group):
        wd = self.app.wd
        app = self.app
        app.pages.open_page(page_name="groups")
        # select the first group
        wd.find_element_by_name("selected[]").click()
        # edit the name of the first group
        wd.find_element_by_xpath("//input[@name='edit']").click()
        wd.find_element_by_name(group.field).clear()
        wd.find_element_by_name(group.field).send_keys(group.name)
        # confirm the change
        wd.find_element_by_name("update").click()
        app.pages.open_page(page_name="group page")
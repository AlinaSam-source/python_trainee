from model.group import Group

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()


    def return_to_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("group page").click()


    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()

        wd.find_element_by_name("new").click()
        self.fill_group_data(group)
        wd.find_element_by_name("submit").click()

        self.return_to_groups_page()
        self.group_cache = None


    def fill_group_data(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            element = wd.find_element_by_name(field_name)
            element.click()
            element.clear()
            element.send_keys(text)


    def delete(self):
        wd = self.app.wd
        self.open_groups_page()

        element_to_delete = self.select_the_first_group()
        group_to_delete = self.resolve_group(element_to_delete)
        element_to_delete.find_element_by_name('selected[]').click()
        wd.find_element_by_name("delete").click()

        self.return_to_groups_page()
        self.group_cache = None
        return group_to_delete



    def select_the_first_group(self):
        wd = self.app.wd
        return wd.find_elements_by_css_selector("span.group")[0]


    def select_the_group_by_id(self, id):
        wd = self.app.wd
        return wd.find_elements_by_css_selector('span.group input[value="%s"]' % id)[0]


    def edit_group(self, group_data):
        wd = self.app.wd
        self.open_groups_page()

        element_to_edit = self.select_the_group_by_id(group_data.id)
        element_to_edit.click()
        wd.find_element_by_xpath("//input[@name='edit']").click()
        self.fill_group_data(group_data)
        wd.find_element_by_name("update").click()

        self.return_to_groups_page()
        self.group_cache = None


    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))


    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()

            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                self.group_cache.append(self.resolve_group(element))

        return list(self.group_cache)


    def resolve_group(self, element):
        text = element.text
        id = element.find_element_by_name("selected[]").get_attribute("value")
        return Group(name=text, id=id)




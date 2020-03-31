class PagesHelper:
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/group.php")

    def open_page(self, page_name):
        wd = self.app.wd
        wd.find_element_by_link_text(page_name).click()
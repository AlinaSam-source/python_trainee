from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from fixture.pages import PagesHelper
from fixture.confirmations import  ConfirmationHelper

class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.pages = PagesHelper(self)
        self.confirmations = ConfirmationHelper(self)

    def destroy(self):
        self.wd.quit()
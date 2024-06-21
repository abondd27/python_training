from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from selenium.webdriver.common.by import By


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not (len(wd.find_elements(By.NAME, "add")) > 0):
            wd.get("http://localhost/addressbook/")

    def return_to_homepage(self):
        wd = self.wd
        if not (len(wd.find_elements(By.NAME, "add")) > 0):
            wd.find_element(By.LINK_TEXT, "home page").click()

    def destroy(self):
        self.wd.quit()

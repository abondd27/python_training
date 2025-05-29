from selenium import webdriver
from random import choice
from selenium.webdriver.support.wait import WebDriverWait
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from selenium.webdriver.common.by import By


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)
        self.wait = WebDriverWait(self.wd, 30)
        self.group = GroupHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not (len(wd.find_elements(By.NAME, "add")) > 0):
            wd.get(self.base_url)

    def return_to_homepage(self):
        wd = self.wd
        if not (len(wd.find_elements(By.NAME, "add")) > 0):
            wd.find_element(By.LINK_TEXT, "home page").click()


    def go_to_home(self):
        wd = self.wd
        if not (wd.find_elements(By.XPATH, "//div[4]/div/form/input") and len(wd.find_elements(By.NAME,"add")) == 0):
            wd.find_element(By.XPATH,"//div[3]/ul/li[1]").click()

    def destroy(self):
        self.wd.quit()

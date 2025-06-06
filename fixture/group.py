from selenium.webdriver.common.by import By
from model.group import Group
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GroupHelper:

    def __init__(self, app):
        self.app = app
        self.wait = app.wait

    def return_to_groups_page(self):
        wd = self.app.wd
        element = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "group page")))
        element.click()

    def create(self, group):
        wd = self.app.wd
        # Init Group Creation
        self.open_groups_page()
        wd.find_element(By.NAME, "new").click()
        # Fill Group Form
        self.fill_group_form(group)
        # Submit Group Creation
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def fill_group_form(self, group):
        wd = self.app.wd
        self.type("group_name", group.name)
        self.type("group_header", group.header)
        self.type("group_footer", group.footer)

    def type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements(By.NAME, "new")) > 0):
            wd.find_element(By.LINK_TEXT, "groups").click()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def modify_first_group(self, new_group_data):
        self.modify_group_by_index(0)

    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        # Init Group Edition
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element(By.NAME, "edit").click()
        # Fill Group Form
        self.fill_group_form(new_group_data)
        # Submit Group Edition
        wd.find_element(By.NAME, "update").click()
        # Return to Groups Page
        self.return_to_groups_page()
        self.group_cache = None

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements(By.CSS_SELECTOR, "span.group"):
                text = element.text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)


    def get_new_group_id(self):
        wd = self.app.wd
        # Получаем список всех элементов групп и берём последний (новый) ID
        groups = wd.find_elements(By.CSS_SELECTOR, "span.group")
        if not groups:
            return None
        last_group = groups[-1]
        return int(last_group.find_element(By.NAME, "selected[]").get_attribute("value"))

    def delete_all_groups(self):
        wd = self.app.wd
        self.open_groups_page()
        # Выделяем все группы
        wd.find_element(By.CSS_SELECTOR, "input[name='selected[]']").click()
        # Удаляем
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()


    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()
        self.group_cache = None


    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "input[value='%s']" %id).click()
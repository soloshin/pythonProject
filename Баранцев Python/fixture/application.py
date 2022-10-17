from selenium import webdriver
from selenium.webdriver.common.by import By

class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def logout(self):
        # Разлогиниваемся
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_groupse_page(self):
        # Возвращаемся на страницу групп
        self.driver.find_element(By.LINK_TEXT, "group page").click()

    def create_group(self, group):
        self.open_groups_page()
        # Создаем новую группу
        self.driver.find_element(By.NAME, "new").click()
        # Заполняем форму
        self.driver.find_element(By.NAME, "group_name").click()
        self.driver.find_element(By.NAME, "group_name").send_keys(group.name)
        self.driver.find_element(By.NAME, "group_header").click()
        self.driver.find_element(By.NAME, "group_header").send_keys(group.header)
        self.driver.find_element(By.NAME, "group_footer").click()
        self.driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # Нажимаем submit и создаем группу
        self.driver.find_element(By.NAME, "submit").click()
        self.return_to_groupse_page()

    def open_groups_page(self):
        # Открываем страницу групп
        self.driver.find_element(By.LINK_TEXT, "groups").click()

    def login(self, user_name, password):
        # login
        self.open_home_page()
        self.driver.set_window_size(1552, 840)
        self.driver.find_element(By.NAME, "user").send_keys(user_name)
        self.driver.find_element(By.NAME, "pass").click()
        self.driver.find_element(By.NAME, "pass").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def open_home_page(self):
        # Открытие страницы
        self.driver.get("http://addressbook/addressbook/")

    def destroy(self):
        self.driver.quit()
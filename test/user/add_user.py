import pytest



from data.login import login_data
from halaman.base.base_page import BasePage
from halaman.login.login_page import LoginPage
from halaman.admin.system_user import SystemUsers
from selenium import webdriver
import time


@pytest.mark.smoke
class TestAddUser:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.base_page = BasePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.system_users = SystemUsers(self.driver)

    def test_login_with_super_admin(self):
        self.base_page.visit()
        self.login_page.fill_login_form(**login_data.super_admin_credential)
        assert self.base_page.is_element_visible(*self.login_page._welcome_button) is True
        self.base_page.wait_visibility_element(*self.system_users._admin_menu)

    def test_access_system_users_menu(self):
        self.system_users.access_system_users_menu()

    def teardown_class(self):
        self.driver.close()
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

from swag_labs_tests.pages.login_page import Login_Page

@pytest.mark.usefixtures("driver")
class TestLogin:

    def setup_class(self):
        self.log_page = Login_Page(self.driver)

    def test_login_locked(self):
        self.log_page.complete_login("locked_out_user", "secret_sauce")
        assert(self.driver.find_element(By.XPATH, '//h3[@data-test="error"]').text == "Epic sadface: Sorry, this user has been locked out.","Error message of locked user is incorrect.")
        self.log_page.clean_user_filed()
        self.log_page.clean_password_field()

    def test_with_invalid_user(self):
        self.driver.refresh()
        self.log_page.complete_login("dummy_user", "dummy_password")
        assert (self.driver.find_element(By.XPATH, '//h3[@data-test="error"]').text == "Epic sadface: Username and password do not match any user in this service")

    def test_login_pass(self):
        self.driver.refresh()
        self.log_page.complete_login("standard_user", "secret_sauce")
        assert(self.driver.find_element(By.XPATH, '//div[@class="app_logo"]').text == "Swag Labs", "App name is not displayed correctly.")
        assert(self.driver.current_url == 'https://www.saucedemo.com/inventory.html', 'Login did not redirect correctly.')



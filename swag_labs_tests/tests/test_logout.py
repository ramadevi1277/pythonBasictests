from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from swag_labs_tests.pages.login_page import Login_Page

@pytest.mark.usefixtures("driver")
class TestLogout:

    def setup_class(self):
        self.log_page = Login_Page(self.driver)

    def test_log_out(self):
        self.log_page.complete_login("standard_user", "secret_sauce")
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        self.driver.find_element(By.ID, "logout_sidebar_link").click()
        assert (self.driver.current_url == "https://www.saucedemo.com/", "Logout not happen successfully.")
from selenium.webdriver.common.by import By

from config.config import TestData
from pages.BasePage import BasePage

from pages.HomePage import HomePage


class LoginPage(BasePage):
    EMAIL_ID = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginbtn")
    SIGNUP_LINK = (By.LINK_TEXT, "Sing Up")

    """constructor of the base class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page Actions...."""

    def get_login_page_title(self, title):
        return self.get_title(title)

    def is_signup_link_existed(self):
        return self.is_visible(self.SIGNUP_LINK)

    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL_ID, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        ####linking login_page with home_page pages
        return HomePage(self.driver)

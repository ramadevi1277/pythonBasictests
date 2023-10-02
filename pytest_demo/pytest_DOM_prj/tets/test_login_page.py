from tets.TestBase import BaseClass
from pages.LoginPage import LoginPage
from config.config import TestData
import time

import pytest

class Test_Login(BaseClass):

    def test_login(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)

    def test_signup_link_visible(self):
          #time.sleep(30)
          self.login_page = LoginPage(self.driver)
          flag = self.login_page.is_signup_link_existed()
          assert flag

    def test_login_page_title(self):
          self.login_page = LoginPage(self.driver)
          title = self.login_page.get_title(TestData.LOGIN_PAGE_TITLE)
          assert title == TestData.LOGIN_PAGE_TITLE



from config.config import TestData
from tets.TestBase import BaseClass
from pages.LoginPage import LoginPage

class Test_Home(BaseClass):

    def test_home_page_title(self):
        self.login_page = LoginPage(self.driver)
        home_page = self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        title = home_page.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE



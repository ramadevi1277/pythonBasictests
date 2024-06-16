from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from swag_labs_tests.pages.checkout_page import Checkout_Page
from swag_labs_tests.pages.inventory_page import Inventory_Page
from swag_labs_tests.pages.login_page import Login_Page

@pytest.mark.usefixtures("driver")
class TestCheckOutErros:

    def setup_class(self):
        self.log_page = Login_Page(self.driver)
        self.checkout_page = Checkout_Page(self.driver)
        self.invent_page = Inventory_Page(self.driver)
        self.log_page.complete_login("standard_user", "secret_sauce")

    def test_errors_on_check_out_page(self):
        self.invent_page.add_item_to_cart_by_index(0)
        self.invent_page.add_item_to_cart_by_index(1)
        self.invent_page.access_cart()
        self.invent_page.go_to_checkout()
        self.checkout_page.continue_to_checkout_overview()
        assert (self.driver.find_element(By.XPATH, '//h3[@data-test="error"]').text == 'Error: First Name is required', 'not seen error')

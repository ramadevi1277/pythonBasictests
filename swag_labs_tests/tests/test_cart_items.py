from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

#from swag_labs_tests.pages.checkout_page import Checkout_Page
from swag_labs_tests.pages.inventory_page import Inventory_Page
from swag_labs_tests.pages.login_page import Login_Page

@pytest.mark.usefixtures("driver")
class Testcartitems:

    def setup_class(self):
        self.log_page = Login_Page(self.driver)
    #    self.checkout_page = Checkout_Page(self.driver)
        self.invent_page = Inventory_Page(self.driver)
        self.log_page.complete_login("standard_user", "secret_sauce")

    def test_items_remove_in_cart(self):
        self.invent_page.add_item_to_cart_by_index(0)
        self.invent_page.add_item_to_cart_by_index(1)
        self.invent_page.access_cart()
        total_links = self.driver.find_elements(By.XPATH, "//div[@class=cart_item_label]//a")
        assert (total_links == 2, "Items added in cart are not correct")
        self.driver.find_element(By.XPATH, "//button[@id='remove-sauce-labs-backpack']").click()
        total_links_after_rmv = self.driver.find_elements(By.XPATH, "//div[@class=cart_item_label]//a")
        assert(total_links_after_rmv == 1, 'items not removed properly')




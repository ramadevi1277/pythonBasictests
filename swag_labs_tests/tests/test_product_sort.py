from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

from swag_labs_tests.pages.inventory_page import Inventory_Page
from swag_labs_tests.pages.login_page import Login_Page

@pytest.mark.usefixtures("driver")
class TestProductSort:

    def setup_class(self):
        self.log_page = Login_Page(self.driver)
        self.log_page.complete_login("standard_user", "secret_sauce")
        self.inv_page = Inventory_Page(self.driver)

    def test_default_sort(self):
        items_titles = self.inv_page.get_inventory_items_titles()
        sorted_items_titles = items_titles.copy()
        sorted_items_titles.sort()

        assert(self.inv_page.get_sort_type_text() == 'Name (A to Z)', 'Default order is not correct.')
        assert(items_titles == sorted_items_titles, "Items are not correctly ordered.")

    def test_invert_named_sort(self):
        self.inv_page.select_sort_type_by_text('Name (Z to A)')

        items_titles = self.inv_page.get_inventory_items_titles()
        reverse_sorted_items_titles = items_titles.copy()
        reverse_sorted_items_titles.sort()
        reverse_sorted_items_titles.reverse()

        assert (items_titles == reverse_sorted_items_titles, "Items are not correctly ordered.")
        assert (self.inv_page.get_sort_type_text() == 'Name (Z to A)', 'Selected order is not correct.')

    def test_sort_price_low_high(self):
        self.inv_page.select_sort_type_by_text('Price (low to high)')

        items_prices = self.inv_page.get_inventory_items_prices()
        sorted_items_prices = items_prices.copy()
        sorted_items_prices.sort()

        assert (self.inv_page.get_sort_type_text() == 'Price (low to high)', 'Order is not the selected one.')
        assert (items_prices == sorted_items_prices, "Items are not correctly ordered by price (low to high).")

    def test_sort_price_high_low(self):
        self.inv_page.select_sort_type_by_text('Price (high to low)')

        items_prices = self.inv_page.get_inventory_items_prices()
        sorted_reverse_items_prices = items_prices.copy()
        sorted_reverse_items_prices.sort()
        sorted_reverse_items_prices.reverse()

        assert (self.inv_page.get_sort_type_text() == 'Price (high to low)', 'Order is not the selected one.')
        assert (items_prices == sorted_reverse_items_prices, "Items are not correctly ordered by price (high to low).")
        assert ('String' == 'Another String', 'Sample assert error.')


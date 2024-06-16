from swag_labs_tests.SLH.slh import SLH
import re

class Checkout_Page:
    def __init__(self, driver):
        self.slh = SLH(driver)

    def set_first_name(self, first_name):
        self.slh.insert_text_by_id('first-name', first_name)

    def set_last_name(self, last_name):
        self.slh.insert_text_by_id('last-name', last_name)

    def set_zip_postal_code(self, zip_postal_code):
        self.slh.insert_text_by_id('postal-code', zip_postal_code)

    def continue_to_checkout_overview(self):
        self.slh.click_element_by_id('continue')

    def fulfill_checkout_informantion(self, first_name, last_name, zip_postal_code):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_zip_postal_code(zip_postal_code)
        self.continue_to_checkout_overview()

    def continue_to_checkout_overview(self):
        self.slh.click_element_by_id('continue')

    def get_total_value(self):
        text_n_value = self.slh.get_text_by_class('summary_subtotal_label')
        value = float(re.search(r'\d+\.\d+', text_n_value).group())
        return value

    def finish_overview(self):
        self.slh.click_element_by_id('finish')

    def get_checkout_status_message(self):
        self.slh.get_text_by_class('title')

    def get_checkout_complete_message(self):
        self.slh.get_text_by_class('complete-header')
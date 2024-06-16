from swag_labs_tests.SLH.slh import SLH

class Login_Page:
    def __init__(self, driver):
        self.slh = SLH(driver)

    def set_login(self, username):
        self.slh.insert_text_by_id("user-name", username)

    def clean_user_filed(self):
        self.slh.clean_text_by_id("user-name")

    def clean_password_field(self):
        self.slh.clean_text_by_id("password")

    def set_password(self, password):
        self.slh.insert_text_by_id("password", password)

    def click_login_button(self):
        self.slh.click_element_by_id("login-button")

    def complete_login(self, username, password):
        self.slh.insert_text_by_id("user-name", username)
        self.slh.insert_text_by_id("password", password)
        self.slh.click_element_by_id("login-button")
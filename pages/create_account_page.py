from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import create_account_page_locators as loc


class CustomerCreateAccount(BasePage):
    page_url = '/customer/account/create/'

    def fill_info_create_account(self, first_name, last_name, email, password, confirm_password):
        self.find(loc.first_name_locator).send_keys(first_name)
        self.find(loc.last_name_locator).send_keys(last_name)
        self.find(loc.email_locator).send_keys(email)
        self.find(loc.password_locator).send_keys(password)
        self.find(loc.confirm_password_locator).send_keys(confirm_password)
        self.find(loc.create_account_button_locator).click()

    def logout(self):
        self.find(loc.account_dropdown_locator).click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(loc.logout_button_locator)
        )
        self.find(loc.logout_button_locator).click()

    def check_create_account_success_message(self, text):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(loc.message_success_locator)
        )
        assert self.find(loc.message_success_locator).text == text

    def check_already_created_account_message(self, text):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(loc.already_created_message_locator)
        )
        assert self.find(loc.already_created_message_locator).text == text

    def check_required_field(self, field, text):
        if field == 'first_name':
            assert self.find(loc.first_name_required_locator).text == text
        elif field == 'last_name':
            assert self.find(loc.last_name_required_locator).text == text
        elif field == 'email':
            assert self.find(loc.email_required_locator).text == text
        elif field == 'password':
            assert self.find(loc.password_required_locator).text == text
        elif field == 'confirm_password':
            assert self.find(loc.confirm_password_required_locator).text == text

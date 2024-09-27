from playwright.sync_api import expect
from test_website_kkaplina_playwrite.pages.base_page import BasePage
from test_website_kkaplina_playwrite.pages.locators import create_account_page_locators as loc


class CustomerCreateAccount(BasePage):
    page_url = '/customer/account/create/'

    def fill_info_create_account(self, first_name, last_name, email, password, confirm_password):
        self.find(loc.first_name_locator).fill(first_name)
        self.find(loc.last_name_locator).fill(last_name)
        self.find(loc.email_locator).fill(email)
        self.find(loc.password_locator).fill(password)
        self.find(loc.confirm_password_locator).fill(confirm_password)
        self.find(loc.create_account_button_locator).click()

    def logout(self):
        self.find(loc.account_dropdown_locator).nth(0).click()
        self.find(loc.logout_button_locator).nth(0).click()

    def check_create_account_success_message(self, text):
        expect(self.find(loc.message_success_locator)).to_have_text(text)

    def check_already_created_account_message(self, text):
        expect(self.find(loc.already_created_message_locator)).to_have_text(text)

    def check_required_field(self, field, text):
        if field == 'first_name':
            expect(self.find(loc.first_name_required_locator)).to_have_text(text)
        elif field == 'last_name':
            expect(self.find(loc.last_name_required_locator)).to_have_text(text)
        elif field == 'email':
            expect(self.find(loc.email_required_locator)).to_have_text(text)
        elif field == 'password':
            expect(self.find(loc.password_required_locator)).to_have_text(text)
        elif field == 'confirm_password':
            expect(self.find(loc.confirm_password_required_locator)).to_have_text(text)

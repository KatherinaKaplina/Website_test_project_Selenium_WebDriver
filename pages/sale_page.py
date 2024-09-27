from test_website_kkaplina_playwrite.pages.base_page import BasePage
from test_website_kkaplina_playwrite.pages.locators import sale_page_locators as loc1
from test_website_kkaplina_playwrite.pages.locators import women_sale_locators as loc2
from test_website_kkaplina_playwrite.pages.locators import jackets_page_locators as loc3
from playwright.sync_api import expect


class SalePage(BasePage):
    page_url = '/sale.html'

    def check_page_header(self, text):
        header_title = self.find(loc1.sale_header_locator)
        expect(header_title).to_have_text(text)

    def check_women_deal_subtitle(self, text):
        subtitle = self.find(loc1.women_sale_subtitle_locator)
        expect(subtitle).to_have_text(text)

    def check_women_deal_link(self, text):
        self.find(loc1.women_sale_link_locator).click()
        women_sale_header = self.find(loc2.women_sale_header_locator)
        expect(women_sale_header).to_have_text(text)

    def check_menu_women_jackets_link(self):
        jackets = self.find(loc1.menu_jacket_women_locator)
        jackets_name = jackets.text_content()
        jackets.click()
        jackets_header = self.find(loc3.jacket_header_locator)
        expect(jackets_header).to_have_text(jackets_name)

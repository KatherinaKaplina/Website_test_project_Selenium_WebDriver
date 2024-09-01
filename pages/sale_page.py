from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import sale_page_locators as loc1
from pages.locators import women_sale_locators as loc2
from pages.locators import jackets_page_locators as loc3


class SalePage(BasePage):
    page_url = '/sale.html'

    def check_page_header(self, text):
        header_title = self.find(loc1.sale_header_locator)
        assert header_title.text == text

    def check_women_deal_subtitle(self, text):
        subtitle = self.find(loc1.women_sale_subtitle_locator)
        assert subtitle.text == text

    def check_women_deal_link(self, text):
        self.find(loc1.women_sale_link_locator).click()
        women_sale_header = self.find(loc2.women_sale_header_locator)
        assert women_sale_header.text == text

    def check_menu_women_jackets_link(self):
        jackets = self.find(loc1.menu_jacket_women_locator)
        jackets_name = jackets.text
        jackets.click()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(loc3.jacket_header_locator)
        )
        jackets_header = self.find(loc3.jacket_header_locator)
        assert jackets_name == jackets_header.text

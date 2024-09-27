from test_website_kkaplina_playwrite.pages.base_page import BasePage
from test_website_kkaplina_playwrite.pages.locators import eco_friendly_page_locators as loc
from playwright.sync_api import expect


class EcoFriendlyPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    def check_compare_first_product(self):
        self.page.wait_for_load_state("networkidle")
        first_product = self.find(loc.first_product_locator).nth(0)
        first_product_name = first_product.text_content().strip()
        compare_button = self.find(loc.compare_button_locator).nth(0)
        first_product.hover()
        compare_button.click()
        self.page.wait_for_selector(loc.compare_products_sidebar_locator)
        compare_sidebar = self.find(loc.compare_products_sidebar_locator)
        expect(compare_sidebar).to_contain_text(first_product_name)

    def check_empty_cart_message(self, text):
        self.find(loc.cart_locator).click()
        expect(self.find(loc.cart_dialog_locator)).to_have_text(text)

    def check_sort_by_price(self):
        sorting_dropdown = self.find(loc.sorting_dropdown_locator).nth(0)
        sorting_dropdown.select_option(value="price")
        self.page.wait_for_timeout(2000)
        prices_list = self.find(loc.product_price_locator).all()
        prices = [float(price.text_content().strip().replace('$', '').replace(',', '')) for price in prices_list]
        assert prices == sorted(prices)

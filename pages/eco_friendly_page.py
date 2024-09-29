from pages.base_page import BasePage
from pages.locators import eco_friendly_page_locators as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class EcoFriendlyPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    def check_compare_first_product(self):
        first_product = self.find(loc.first_product_locator)
        compare_button = self.find(loc.compare_button_locator)
        first_product_name = first_product.text

        ActionChains(self.driver).move_to_element(first_product).click(compare_button).perform()

        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(loc.compare_products_sidebar_locator)
        )
        assert self.find(loc.compare_products_sidebar_locator).text == first_product_name

    def check_empty_cart_message(self, text):
        self.find(loc.cart_locator).click()
        assert self.find(loc.cart_dialog_locator).text == text

    def check_sort_by_price(self):
        select = self.find(loc.sorting_dropdown_locator)
        dropdown = Select(select)
        dropdown.select_by_value('price')
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(loc.product_price_locator)
        )
        prices_list = self.find_all(loc.product_price_locator)
        prices = []
        for i in prices_list:
            price = i.text
            prices.append(float(price.replace('$', '').replace(',', '')))
        assert prices == sorted(prices)

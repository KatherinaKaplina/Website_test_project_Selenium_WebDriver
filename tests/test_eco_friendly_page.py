import allure
import pytest


@allure.title('First product appears in Compare Products section')
@pytest.mark.smoke
def test_compare_first_product(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.check_compare_first_product()


@allure.title('Message for empty cart')
@pytest.mark.regression
def test_empty_cart_message(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.check_empty_cart_message('You have no items in your shopping cart.')


@allure.title('Sorting by price is working')
@pytest.mark.regression
def test_sort_by_price(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.check_sort_by_price()

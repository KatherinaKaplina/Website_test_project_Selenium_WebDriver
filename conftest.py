from selenium import webdriver
import pytest
from pages.sale_page import SalePage
from pages.create_account_page import CustomerCreateAccount
from pages.eco_friendly_page import EcoFriendlyPage


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-search-engine-choice-screen")
    chrome_driver = webdriver.Chrome(options=options)
    return chrome_driver


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture()
def create_account_page(driver):
    return CustomerCreateAccount(driver)

@pytest.fixture()
def eco_friendly_page(driver):
    return EcoFriendlyPage(driver)

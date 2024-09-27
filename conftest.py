import pytest
from test_website_kkaplina_playwrite.pages.sale_page import SalePage
from test_website_kkaplina_playwrite.pages.create_account_page import CustomerCreateAccount
from test_website_kkaplina_playwrite.pages.eco_friendly_page import EcoFriendlyPage
from playwright.sync_api import BrowserContext


@pytest.fixture()
def page(context: BrowserContext):
    page = context.new_page()
    page.set_viewport_size({'width': 1280, 'height': 1080})
    return page


@pytest.fixture()
def sale_page(page):
    return SalePage(page)


@pytest.fixture()
def create_account_page(page):
    return CustomerCreateAccount(page)


@pytest.fixture()
def eco_friendly_page(page):
    return EcoFriendlyPage(page)

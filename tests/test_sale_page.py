import allure


@allure.title('Sale header')
def test_header_title(sale_page):
    sale_page.open_page()
    sale_page.check_page_header('Sale')


@allure.title('Women’s Deals block subtitle')
def test_women_deal_subtitle(sale_page):
    sale_page.open_page()
    sale_page.check_women_deal_subtitle('Pristine prices on pants, tanks and bras.')


@allure.title('Women’s Deals block link is working')
def test_women_deal_link(sale_page):
    sale_page.open_page()
    sale_page.check_women_deal_link('Women Sale')


@allure.title('Women’s Deals menu jackets link is working')
def test_menu_women_jackets_link(sale_page):
    sale_page.open_page()
    sale_page.check_menu_women_jackets_link()

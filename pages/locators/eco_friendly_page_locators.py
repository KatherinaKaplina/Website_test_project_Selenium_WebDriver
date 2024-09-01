from selenium.webdriver.common.by import By


jacket_header_locator = (By.TAG_NAME, 'h1')
first_product_locator = (By.XPATH, '//*[@class="product-item-link"][1]')
last_product_locator = (By.XPATH, '//*[@class="product-item-link"][12]')
compare_button_locator = (By.XPATH, '//*[@class="action tocompare"][1]')
compare_products_sidebar_locator = (By.CSS_SELECTOR, '.product-item.odd.last strong a')
cart_locator = (By.CSS_SELECTOR, '.action.showcart')
cart_dialog_locator = (By.CSS_SELECTOR, '.subtitle.empty')
sorting_dropdown_locator = (By.ID, 'sorter')
product_price_locator = (By.CSS_SELECTOR, '.price-wrapper ')

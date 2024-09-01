from selenium.webdriver.common.by import By


first_name_locator = (By.ID, 'firstname')
last_name_locator = (By.ID, 'lastname')
email_locator = (By.ID, 'email_address')
password_locator = (By.ID, 'password')
confirm_password_locator = (By.ID, 'password-confirmation')
create_account_button_locator = (By.XPATH, '//*[@class="action submit primary"]')

email_success_locator = (By.CSS_SELECTOR, '[class="box-content"] > p > br')
message_success_locator = (By.XPATH, '//*[@data-ui-id="message-success"]')

already_created_message_locator = (By.XPATH, '//*[@data-ui-id="message-error"]')

account_dropdown_locator = (By.XPATH, '//*[@class="action switch"]')
logout_button_locator = (By.CSS_SELECTOR, 'li[class="authorization-link"] > a')

first_name_required_locator = (By.ID, 'firstname-error')
last_name_required_locator = (By.ID, 'lastname-error')
email_required_locator = (By.ID, 'email_address-error')
password_required_locator = (By.ID, 'password-error')
confirm_password_required_locator = (By.ID, 'password-confirmation-error')

import pytest
from test_data import (TEST_DATA_CREATE_ACCOUNT, NEGATIVE_DATA_CREATE_ACCOUNT)
import allure


@allure.title('Create account')
@pytest.mark.smoke
def test_create_account_success_message(create_account_page):
    create_account_page.open_page()
    create_account_page.fill_info_create_account(
        TEST_DATA_CREATE_ACCOUNT['first_name'],
        TEST_DATA_CREATE_ACCOUNT['last_name'],
        TEST_DATA_CREATE_ACCOUNT['email'],
        TEST_DATA_CREATE_ACCOUNT['password'],
        TEST_DATA_CREATE_ACCOUNT['confirm_password']
    )
    create_account_page.check_create_account_success_message('Thank you for registering with Main Website Store.')
    create_account_page.logout()


@allure.title('Message when account is already created')
@pytest.mark.regression
def test_already_created_account_message(create_account_page):
    create_account_page.open_page()
    create_account_page.fill_info_create_account(
        TEST_DATA_CREATE_ACCOUNT['first_name'],
        TEST_DATA_CREATE_ACCOUNT['last_name'],
        TEST_DATA_CREATE_ACCOUNT['email'],
        TEST_DATA_CREATE_ACCOUNT['password'],
        TEST_DATA_CREATE_ACCOUNT['confirm_password']
    )
    create_account_page.check_already_created_account_message(
        'There is already an account with this email address. '
        'If you are sure that it is your email address, click here to get your password and access your account.'
    )


@allure.title('Required fields test')
@pytest.mark.extended
@pytest.mark.parametrize('data', NEGATIVE_DATA_CREATE_ACCOUNT)
def test_required_field_first_name(create_account_page, data):
    create_account_page.open_page()
    create_account_page.fill_info_create_account(
        data['first_name'],
        data['last_name'],
        data['email'],
        data['password'],
        data['confirm_password']
    )
    if data['first_name'] == '':
        create_account_page.check_required_field('first_name', 'This is a required field.')
    elif data['last_name'] == '':
        create_account_page.check_required_field('last_name', 'This is a required field.')
    elif data['email'] == '':
        create_account_page.check_required_field('email', 'This is a required field.')
    elif data['password'] == '':
        create_account_page.check_required_field('password', 'This is a required field.')
    elif data['confirm_password'] == '':
        create_account_page.check_required_field('confirm_password', 'This is a required field.')

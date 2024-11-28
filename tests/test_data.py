import random

random_number = random.randint(11, 100)
TEST_DATA_CREATE_ACCOUNT = {
    "first_name": f"Kate_{random_number}",
    "last_name": f"Test_{random_number}",
    "email": f"kate_{random_number}@test.test",
    "password": "123QWqw!",
    "confirm_password": "123QWqw!"
}

NEGATIVE_DATA_CREATE_ACCOUNT = [
    {
        'first_name': '',
        'last_name': 'Test_100',
        'email': 'kate_100@test.test',
        'password': '123QWqw!',
        'confirm_password': '123QWqw!'
    },
    {
        'first_name': 'Kate_100',
        'last_name': '',
        'email': 'kate_100@test.test',
        'password': '123QWqw!',
        'confirm_password': '123QWqw!'
    },
    {
        'first_name': 'Kate_100',
        'last_name': 'Test_100',
        'email': '',
        'password': '123QWqw!',
        'confirm_password': '123QWqw!'
    },
    {
        'first_name': 'Kate_100',
        'last_name': 'Test_100',
        'email': 'kate_100@test.test',
        'password': '',
        'confirm_password': '123QWqw!'
    },
    {
        'first_name': 'Kate_100',
        'last_name': 'Test_100',
        'email': 'kate_100@test.test',
        'password': '123QWqw!',
        'confirm_password': ''
    }
]


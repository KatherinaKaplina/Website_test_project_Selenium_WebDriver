TEST_DATA_CREATE_ACCOUNT = {
    "first_name": "Kate_101",
    "last_name": "Test_101",
    "email": "kate_101@test.test",
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

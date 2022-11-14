"""
This module encapsulates details about users.
"""

TEST_USER_NAME = 'Test user'
USERNAME = 'username'
PASSWORD = 'password'

# We expect the user database to change frequently:
# For now, we will consider EMAIL to be
# our mandatory fields.
REQUIRED_FLDS = [USERNAME, PASSWORD]
users = {TEST_USER_NAME: {USERNAME: 'user1@gmail.com', PASSWORD: 'test123'},
         'handle': {USERNAME: 'user2@gmail.com', PASSWORD: 'test234'}}


def user_exists(username):
    """
    Returns whether or not a user exists.
    """
    return username in users


def get_users():
    return list(users.keys())


def get_users_dict():
    return users


def del_user(username):
    del users[username]


def add_user(username, password):
    if not isinstance(username, str):
        raise TypeError(f'Wrong type for username: {type(username)}')
    if not isinstance(password, dict):
        raise TypeError(f'Wrong type for password: {type(password)}')
    for field in REQUIRED_FLDS:
        if field not in password:
            raise ValueError(f'Required {field} missing from details.')
    users[username] = password


def main():
    users = get_users()
    print(f'{users}')
    print(f'{get_user_details(TEST_USER_NAME)}')


"""
This module encapsulates details about users.
"""

TEST_USER_NAME = 'Test user'
NAME = 'name'
EMAIL = 'email'
FULL_NAME = 'full_name'

# We expect the user database to change frequently:
# For now, we will consider EMAIL to be
# our mandatory fields.
REQUIRED_FLDS = [EMAIL]
users = {TEST_USER_NAME: {EMAIL: 'x@y.com', FULL_NAME: 'Porgy Tirebiter'},
         'handle': {EMAIL: 'z@y.com', FULL_NAME: 'Nick Danger'}}

def user_exists(username):
    return username in users

def get_users():
    return list(users.keys())

def get_user_details(user):
    return users.get(user, None)

def del_user(username):
    del users[username]

def add_user(username, password):
    if not isinstance(username, str):
        raise TypeError(f'Wrong type for username: {type(username)}')
    if not isinstance(password, str):
        raise TypeError(f'Wrong type for username: {type(password)}')
    for field in REQUIRED_FLDS:
        if field not in password:
            raise ValueError(f'Required {field} missing from details.')
        users[username] = password

def main():
    users = get_users()
    print(f'{users}')
    print(f'{get_user_details(TEST_USER_NAME)}')

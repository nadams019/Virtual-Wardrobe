"""
This module encapsulates details about users.
"""

TEST_USER_NAME = 'Test user'
USERNAME = 'name'
EMAIL = 'email'
FULL_NAME = 'full_name'

# We expect the user database to change frequently:
# For now, we will consider EMAIL to be
# our mandatory fields.
REQUIRED_FLDS = [EMAIL]
users = {TEST_USER_NAME: {EMAIL: 'x@y.com', FULL_NAME: 'Porgy Tirebiter'},
         'handle': {EMAIL: 'z@y.com', FULL_NAME: 'Nick Danger'}}


def user_exists(name):
    """
    Returns whether or not a user exists.
    """
    return name in users


def get_users():
    return list(users.keys())


def get_users_dict():
    return users


def get_user_details(user):
    return users.get(user, None)


def del_user(name):
    del users[name]


def add_user(name, details):
    if not isinstance(name, str):
        raise TypeError(f'Wrong type for name: {type(name)=}')
    if not isinstance(details, dict):
        raise TypeError(f'Wrong type for details: {type(details)=}')
    for field in REQUIRED_FLDS:
        if field not in details:
            raise ValueError(f'Required {field=} missing from details.')
    users[name] = details


def main():
    users = get_users()
    print(f'{users=}')
    print(f'{get_user_details(TEST_USER_NAME)=}')


if __name__ == '__main__':
    main()

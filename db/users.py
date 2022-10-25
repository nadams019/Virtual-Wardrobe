TEST_USER_NAME = 'Test user'
USERNAME = 'username'
PASSWORD = 'password'

REQUIRED_FLDS = [USERNAME, PASSWORD]
users = {TEST_USER_NAME: {USERNAME: 'janedoe123', PASSWORD: 'Il0v3comput3r51'},
         'handle': {USERNAME: 'janedoe123', PASSWORD: 'Il0v3comput3r51'}}

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

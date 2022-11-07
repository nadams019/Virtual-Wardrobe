import pytest

import db.users as usr


def test_get_users():
    usrs = usr.get_users()
    assert isinstance(usrs, list)
    assert len(usrs) > 1


def test_get_user_details():
    usr_dets = usr.get_user_details(usr.TEST_USER_NAME)
    assert isinstance(usr_dets, dict)


def test_add_wrong_name_type():
    with pytest.raises(TypeError):
        usr.add_user(7, {})


def test_add_wrong_details_type():
    with pytest.raises(TypeError):
        usr.add_user('a new user', [])


def test_add_missing_field():
    with pytest.raises(ValueError):
        usr.add_user('a new user', {'foo': 'bar'})


def test_add_user():
    details = {}
    for field in usr.REQUIRED_FLDS:
        details[field] = 2
    usr.add_user(usr.TEST_USER_NAME, details)
    assert usr.user_exists(usr.TEST_USER_NAME)
    usr.del_user(usr.TEST_USER_NAME)

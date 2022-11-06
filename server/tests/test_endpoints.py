
import pytest

import db.users as usr

import server.endpoints as ep

TEST_CLIENT = ep.app.test_client()
TEST_USERNAME = 'user1@gmail.com'


def test_hello():
    resp_json = TEST_CLIENT.get(ep.HELLO).get_json()
    assert isinstance(resp_json[ep.MESSAGE], str)


SAMPLE_USER_NM = 'SampleUser'
SAMPLE_USER = {
    usr.username: SAMPLE_USER_NM,
    usr.password: 'test123',
    usr.FULL_NAME: 'Sample user',
}
def test_add_user():
    resp = TEST_CLIENT.post(ep.USER_ADD, json=SAMPLE_USER)
    assert usr.user_exists(SAMPLE_USER_NM)
    usr.del_user(SAMPLE_USER_NM)


def test_get_user_list():
    """
    See if we can get a user list properly.
    Return should look like:
        {USER_LIST_NM: [list of users types...]}
    """
    resp = TEST_CLIENT.get(ep.USER_LIST_W_NS)
    resp_json = resp.get_json()
    assert isinstance(resp_json[ep.USER_LIST_NM], list)




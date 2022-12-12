
import server.endpoints as ep
import db.users as usr
import db.closet_browse as brwse


TEST_CLIENT = ep.app.test_client()
TEST_CLOTHING_TYPE = 'Clothing'


def test_hello():
    """
    See if Hello works.
    """
    resp_json = TEST_CLIENT.get(ep.HELLO).get_json()
    assert isinstance(resp_json[ep.MESSAGE], str)


SAMPLE_USER_NM = 'SampleUser'
SAMPLE_USER = {
    usr.USERNAME: SAMPLE_USER_NM,
    usr.EMAIL: 'x@y.com',
    usr.FULL_NAME: 'Sample User',
}


def test_add_user():
    """
    Test adding a user.
    """
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


SAMPLE_ITEM_NM = 'SampleItem'
SAMPLE_ITEM = {
    brwse.CLOTHING: SAMPLE_ITEM_NM,
    brwse.SEASON: 'Sample Season',
    brwse.OCCASION: 'Sample Occasion',
    brwse.AESTHETIC: 'Sample Aesthetic',
    brwse.RANDOM: 'Sample Bool',
}


def test_add_clothing_post():
    resp = TEST_CLIENT.post(ep.CLOSETBROWSE_ADD, json=SAMPLE_ITEM)
    assert brwse.clothing_exists(SAMPLE_ITEM_NM)
    brwse.del_clothing(SAMPLE_ITEM_NM)


def test_get_clothing_list():
    """
    See if we can get a user list properly.
    Return should look like:
        {CLOSETBROWSE_LIST_NM: [list of users types...]}
    """
    resp_json = TEST_CLIENT.get(ep.CLOSETBROWSE_LIST_W_NS).get_json()
    assert isinstance(resp_json[ep.CLOSETBROWSE_LIST_NM], list)


def test_get_clothing_list_not_empty():
    """
    See if we can get a clothing list properly.
    Return should look like:
        {CHAR_TYPE_LIST_NM: [list of chars types...]}
    """
    resp_json = TEST_CLIENT.get(ep.CLOSETBROWSE_LIST_W_NS).get_json()
    assert len(resp_json[ep.CLOSETBROWSE_LIST_NM]) > 0


def test_get_clothing_details():
    """
    """
    resp_json = TEST_CLIENT.get(f'{ep.CLOSETBROWSE_DETAILS}/{TEST_CLOTHING_TYPE}').get_json()
    assert TEST_CLOTHING_TYPE in resp_json
    assert isinstance(resp_json[TEST_CLOTHING_TYPE], dict)


def test_login():
    response = TEST_CLIENT.get(f'{ep.LOGIN_NS}').get_json()
    assert response.status == "Successful login"

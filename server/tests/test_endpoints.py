
import server.endpoints as ep
import db.users as usr
import db.closet_browse as brwse
import db.browse as br
# import db.aesthetics_types as aes

TEST_CLIENT = ep.app.test_client()
TEST_CLOTHING_TYPE = 'Clothing'
TEST_AES_TYPE = 'Grunge'

SAMPLE_USER_NM = 'SampleUser'
SAMPLE_USER = {
    usr.EMAIL: 'x@y.com',
    usr.FULL_NAME: SAMPLE_USER_NM,
    usr.USERNAME: 'sample_user',
    usr.PASSWORD: 'abcde123'
}


def test_hello():
    """
    See if Hello works.
    """
    resp_json = TEST_CLIENT.get(ep.HELLO).get_json()
    assert isinstance(resp_json[ep.MESSAGE], str)


def test_add_user():
    """
    Test adding a user.
    """
    resp = TEST_CLIENT.post(ep.USER_ADD, json=SAMPLE_USER)
    assert usr.user_exists(SAMPLE_USER_NM)
    usr.del_user(SAMPLE_USER_NM)


def test_add_clothing():
    """
    Test adding a clothing item.
    """
    resp = TEST_CLIENT.post(ep.BROWSE_ADD, json=SAMPLE_ITEM)
    assert br.clothing_exists(SAMPLE_ITEM_NM)
    br.del_clothing(SAMPLE_ITEM)


def test_get_user_list():
    """
    See if we can get a user list properly.
    Return should look like:
        {USER_LIST_NM: [list of users types...]}
    """
    resp = TEST_CLIENT.get(ep.USER_LIST_W_NS)
    resp_json = resp.get_json()
    assert isinstance(resp_json[ep.USER_LIST_NM], list)


def test_get_aesthetic_type_list():
    """
    See if we can get an aesthetic type list properly.
    Return should look like:
        {CHAR_TYPE_LIST_NM: [list of chars types...]}
    """
    resp_json = TEST_CLIENT.get(ep.AES_TYPE_LIST_W_NS).get_json()
    assert isinstance(resp_json[ep.AES_TYPE_LIST_NM], list)


def test_get_aesthetic_type_list_not_empty():
    """
    See if we can get an aesthetic type list properly.
    Return should look like:
        {AES_TYPE_LIST_NM: [list of chars types...]}
    """
    resp_json = TEST_CLIENT.get(ep.AES_TYPE_LIST_W_NS).get_json()
    assert len(resp_json[ep.AES_TYPE_LIST_NM]) > 0


def test_get_aesthetic_type_details():
    """
    """
    resp_json = TEST_CLIENT.get(f'{ep.AES_TYPE_DETAILS_W_NS}/'
                                f'{TEST_AES_TYPE}').get_json()
    assert TEST_AES_TYPE in resp_json
    assert isinstance(resp_json[TEST_AES_TYPE], dict)


SAMPLE_ITEM_NM = 'SampleItem'
SAMPLE_ITEM = {
    brwse.CLOTHING: SAMPLE_ITEM_NM,
    brwse.SEASON: 'Sample Season',
    brwse.OCCASION: 'Sample Occasion',
    brwse.AESTHETIC: 'Sample Aesthetic',
    brwse.RANDOM: 'Sample Bool',
}

'''
def test_add_clothing_post():
    resp = TEST_CLIENT.post(ep.CLOSETBROWSE_ADD, json=SAMPLE_ITEM)
    assert resp.get_json()
    brwse.del_clothing(SAMPLE_ITEM_NM)



def test_get_clothing_list():
    """
    See if we can get a user list properly.
    Return should look like:
        {CLOSETBROWSE_LIST_NM: [list of users types...]}
    """
    resp = TEST_CLIENT.get(ep.CLOSETBROWSE_LIST_W_NS)
    resp_json = resp.get_json()
    assert isinstance(resp_json[ep.CLOSETBROWSE_LIST_NM], list)


def test_get_clothing_details():
    """
    See if we can get clothing details
    """
    resp_json = TEST_CLIENT.get(f'{ep.CLOSETBROWSE_DETAILS_W_NS}/{TEST_CLOTHING_TYPE}').get_json()
    assert TEST_CLOTHING_TYPE in resp_json
    assert isinstance(resp_json[TEST_CLOTHING_TYPE], dict)



def test_login():
    response = TEST_CLIENT.get(f'{ep.LOGIN_NS}').get_json()
    assert response.status == "Successfully logged in"
'''


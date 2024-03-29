import io
import tempfile
import os
from unittest.mock import patch
import db.aesthetics_types as aes
from http import HTTPStatus
import db.closet_browse as brwse
# import db.browse as br
import db.contacts as cnts
import db.users as usr
import db.aesthetics_types as aes
import requests
import server.endpoints as ep

TEST_CLIENT = ep.app.test_client()
TEST_CLOTHING_TYPE = 'Clothing'
TEST_AES_TYPE = 'Grunge'

SAMPLE_USER_NM = 'SampleUser'
SAMPLE_USER = {
    usr.EMAIL: 'x@y.com',
    usr.NAME: SAMPLE_USER_NM,
    usr.FULL_NAME: 'Sample User',
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
    resp = TEST_CLIENT.post(ep.CLOSET_ADD, json=SAMPLE_ITEM)
    assert brwse.clothing_exists(SAMPLE_ITEM_NM)
    brwse.del_clothing(SAMPLE_ITEM_NM)


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


@patch('db.aesthetics_types.get_aes_type_details', return_value=SAMPLE_USER)
def test_get_aesthetic_type_details(mock_get_aesthetic_type_details):
    resp = TEST_CLIENT.get(f'{ep.AES_TYPE_DETAILS_W_NS}/{TEST_AES_TYPE}')
    assert resp.status_code == HTTPStatus.OK
    assert isinstance(resp.json, dict)


SAMPLE_ITEM_NM = 'SampleItem'
SAMPLE_ITEM = {
    brwse.CLOTHING: SAMPLE_ITEM_NM,
    brwse.SEASON: 'Sample Season',
    brwse.OCCASION: 'Sample Occasion',
    brwse.AESTHETIC: 'Sample Aesthetic',
    brwse.RANDOM: 'Sample Bool',
}


def test_add_clothing_post():
    resp = TEST_CLIENT.post(ep.BROWSE_ADD, json=SAMPLE_ITEM)
    assert resp.get_json()
    brwse.del_clothing(SAMPLE_ITEM_NM)


# def test_get_clothing_list():
#     """
#     See if we can get a user list properly.
#     Return should look like:
#         {CLOSETBROWSE_LIST_NM: [list of users types...]}
#     """
#     resp_json = TEST_CLIENT.get(ep.CLOSET_LIST_NM).get_json()
#     assert isinstance(resp_json[ep.CLOSET_LIST_W_NS], list)

# def test_get_clothing_details():
#     """
#     See if we can get clothing details
#     """
#     resp_json = TEST_CLIENT.get(f'{ep.BROWSE_DETAILS_W_NS}/{TEST_CLOTHING_TYPE}').get_json()
#     assert TEST_CLOTHING_TYPE in resp_json
#     assert isinstance(resp_json[TEST_CLOTHING_TYPE], dict)

def test_login():
    with TEST_CLIENT as client:
        # Simulate a POST request with correct credentials
        response = client.post('/login', data=SAMPLE_USER)

        # Expect a redirect status code and check that it goes to the
        # correct page
        assert response.status_code == 302, \
            f"Expected redirect status code, but got {response.status_code}. " \
            f"Response content: {response.data}"

def test_upload_closet():
    with TEST_CLIENT as client:
        data = {
            'item_type': 'dresses',
            'aesthetic': 'grunge',
            'occasion': 'casual',
            'season': 'summer'
        }
        response = client.post('/upload', data=data)
        assert response.status_code == 200
        assert response.data == b'{"message":"Clothing item uploaded ' \
                                b'successfully!","success":true}\n'
'''
def test_upload_file():
    # Set the URL of the file upload endpoint
    url = 'http://localhost:8000/upload'
    # Get the absolute path to the root directory of the repo
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    # Construct the path to the image file
    image_path = os.path.join(root_dir, "server", "templates", "static", "images", "dress.jpeg")
    # Open the file in binary mode and read its contents
    with open(image_path, 'rb') as f:
        file_data = f.read()
    # Set the headers for the HTTP request
    headers = {'Content-Type': 'multipart/form-data'}
    # Set the payload for the HTTP request
    payload = {'file': ('file.txt', file_data)}
    # Make a POST request to the file upload endpoint
    response = requests.post(url, headers=headers, files=payload)
    # Assert that the response status code is 200
    assert response.status_code, 200
    # Assert that the response text contains 'File uploaded successfully'
    assert 'File uploaded successfully' in response.text


def test_closet_upload():
    # Create a temporary file for testing this
    with TEST_CLIENT as client:
        with tempfile.NamedTemporaryFile(suffix='.png', dir=os.path.abspath('path/to/test/upload/folder') as f:
            # Send a POST request to the endpoint with the temporary file
            response = client.post(
                f'/upload/closet/1/upload',
                data={
                    'file': (f.name, open(f.name, 'rb'), 'image/png')
                }
            )
            # Verify that the response status code is 201 (Created)
            assert response.status_code == 201
            # Verify that the response message is what we expect
            assert response.json == {'message': 'File uploaded successfully'}
'''

SAMPLE_CONTACT_NM = 'SampleContact'
SAMPLE_CONTACT = {
    cnts.FULL_NAME: SAMPLE_CONTACT_NM,
    cnts.EMAIL: 'x@y.com',
    cnts.FIRST_NAME: 'Sample',
    cnts.LAST_NAME: 'Contact',
    cnts.REQUEST: 'This is a request.',
}


# developer endpoint
def test_get_contact_list():
    resp = TEST_CLIENT.get(ep.CONTACTS_LIST_W_NS)
    resp_json = resp.get_json()
    assert isinstance(resp_json[ep.CONTACTS_LIST_NM], list)


def test_add_contact():
    """
    Test adding a contact request.
    """
    resp = TEST_CLIENT.post(ep.CONTACTS_ADD, json=SAMPLE_CONTACT)
    assert cnts.contact_exists(SAMPLE_CONTACT_NM)
    cnts.del_contact(SAMPLE_CONTACT_NM)

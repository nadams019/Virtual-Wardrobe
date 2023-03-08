import pytest
import db.contacts as cnt
NEW_CONTACT = 'test name'
@pytest.fixture(scope='function')
def temp_contact():
    cnt.add_contact(NEW_CONTACT, cnt.get_contacts_dict())
    yield
    cnt.del_contact(NEW_CONTACT, cnt.get_contacts_dict())
def test_get_contacts():
    cnts = cnt.get_contacts()
    assert isinstance(cnts, list)
    assert len(cnts)>1

def test_get_contacts_dict():
    cnts = cnt.get_contacts_dict()
    assert isinstance(cnts, dict)
    assert len(cnts) > 1

def test_get_contact_details():
    cnt_dets = cnt.get_contact_details(cnt.NEW_CONTACT)
    assert isinstance(cnt_dets, dict)



def test_add_contact():
    details = {}
    for field in cnt.REQUIRED_FLDS:
        details[field] = 2
    cnt.add_contact(cnt.NEW_CONTACT, details)

@pytest.mark.skip("Can't run this test untill the delete function is written.")
def test_del_contact():
    assert False

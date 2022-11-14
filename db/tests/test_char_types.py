import pytest

import db.char_types as ctyp

NEW_CHAR_TYPE = 'Priest'
DEF_TRAITS = {'health': 7, 'magic': 10}


@pytest.fixture(scope='function')
def new_char_type():
    ctyp.add_char_type(NEW_CHAR_TYPE, DEF_TRAITS)
    # yield is where the test is run!
    yield
    ctyp.del_char_type(NEW_CHAR_TYPE)


def test_get_char_types():
    ct = ctyp.get_char_types()
    assert isinstance(ct, list)
    assert len(ct) > 1


def test_get_char_type_details(new_char_type):
    ctd = ctyp.get_char_type_details(NEW_CHAR_TYPE)
    assert isinstance(ctd, dict)


def test_add_char_type(new_char_type):
    assert ctyp.char_type_exists(NEW_CHAR_TYPE)


def test_add_char_type_dup(new_char_type):
    """
    See if we catch adding a duplicate character type.
    """
    with pytest.raises(ValueError):
        ctyp.add_char_type(NEW_CHAR_TYPE, DEF_TRAITS)


def test_char_type_exists(new_char_type):
    assert ctyp.char_type_exists(NEW_CHAR_TYPE)


def test_char_type_not_exists():
    assert not ctyp.char_type_exists('Some nonsense character type')


@pytest.mark.skip("Can't run this test untill the delete function is written.")
def test_del_char_type():
    assert False
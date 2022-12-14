import pytest

import db.aesthetics_types as ctyp

NEW_AES_TYPE = 'E-Boy'
DEF_TRAITS = {'points': 6}


@pytest.fixture(scope='function')
def new_aes_type():
    ctyp.add_aes_type(NEW_AES_TYPE, DEF_TRAITS)
    # yield is where the test is run!
    yield
    ctyp.del_aes_type(NEW_AES_TYPE)


def test_get_aes_types():
    ct = ctyp.get_aes_types()
    assert isinstance(ct, list)
    assert len(ct) > 1


def test_get_aes_type_details(new_aes_type):
    ctd = ctyp.get_aes_type_details(NEW_AES_TYPE)
    assert isinstance(ctd, dict)


def test_add_aes_type(new_aes_type):
    assert ctyp.aes_type_exists(NEW_AES_TYPE)


def test_add_aes_type_dup(new_aes_type):
    """
    See if we catch adding a duplicate aesthetics type.
    """
    with pytest.raises(ValueError):
        ctyp.add_aes_type(NEW_AES_TYPE, DEF_TRAITS)


def test_aes_type_exists(new_aes_type):
    assert ctyp.aes_type_exists(NEW_AES_TYPE)


def test_aes_type_not_exists():
    assert not ctyp.aes_type_exists('Some nonsense aesthetics type')


@pytest.mark.skip("Can't run this test untill the delete function is written.")
def test_del_aes_type():
    pass
    # assert False
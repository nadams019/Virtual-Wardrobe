import pytest

import db.char_types as ctyp

CHAR_TYPE = 'itemTypeButton'
DEF_SELECTIONS = {'Jewelery', 'Tops'}


@pytest.fixture(scope='function')
def new_char_type():
    ctyp.add_char_type(CHAR_TYPE, DEF_SELECTIONS)
    yield
    ctyp.del_char_type(CHAR_TYPE)


def test_get_char_types():
    ct = ctyp.get_char_types()
    assert isinstance(ct, list)
    assert len(ct) > 1


def test_get_char_type_details(new_char_type):
    ctd = ctyp.get_char_type_details(CHAR_TYPE)
    assert isinstance(ctd, dict)


def test_add_char_type(new_char_type):
    assert ctyp.char_type_exists(CHAR_TYPE)


def test_add_char_type_dup(new_char_type):
    with pytest.raises(ValueError):
        ctyp.add_char_type(CHAR_TYPE, DEF_SELECTIONS)


def test_char_type_exists(new_char_type):
    assert ctyp.char_type_exists(CHAR_TYPE)


def test_char_type_not_exists():
    assert not ctyp.char_type_exists('Some nonsense character type')


@pytest.mark.skip("Can't run this test untill the delete function is written.")
def test_del_char_type():
    assert False
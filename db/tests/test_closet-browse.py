import pytest

import db.closet_browse as browse


def test_get_clothes():
    browsing = browse.get_clothes()
    assert isinstance(browsing, list)
    assert len(browsing) > 1


def test_get_clothing_details():
    browse_dets = browse.get_clothing_details(browse.TEST_GAME_NAME)
    assert isinstance(browse_dets, dict)


def test_add_wrong_name_type():
    with pytest.raises(TypeError):
        browse.add_clothing(7, {})


def test_add_wrong_details_type():
    with pytest.raises(TypeError):
        browse.add_clothing('a new clothing item', [])


def test_add_missing_field():
    with pytest.raises(ValueError):
        browse.add_clothing('a new clothing item', {'foo': 'bar'})


def test_add_clothing():
    details = {}
    for field in browse.REQUIRED_FLDS:
        details[field] = 2
    browse.add_clothing(browse.TEST_GAME_NAME, details)
    assert browse.clothing_exists(browse.TEST_GAME_NAME)

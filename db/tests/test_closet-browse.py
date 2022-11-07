import pytest

import db.closet_browse as browse


def test_get_clothes():
    result = browse.get_clothes()
    assert isinstance(result, list)
    assert len(result) > 1


def test_get_clothing_details():
    cloth_deets = browse.get_clothing_details(browse.TEST_CATEGORY_NAME)
    assert isinstance(cloth_deets, dict)

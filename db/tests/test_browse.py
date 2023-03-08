import os
from copy import deepcopy

import pytest
import db.closet_browse as browse
RUNNING_ON_CICD_SERVER = os.environ.get('CI', False)
TEST_DEL_NAME = 'Item to be deleted'

TEST_DETAILS = {browse.SEASON: 'Fall',
                browse.OCCASION: 'Prom',
                browse.AESTHETIC: 'Punk',
                browse.RANDOM: True}


@pytest.fixture(scope='function')
def temp_closet():
    browse.add_clothing(browse.TEST_CLOTHING_NAME, TEST_DETAILS)
    yield
    browse.del_clothing(browse.TEST_CLOTHING_NAME)


@pytest.fixture(scope='function')
def details():
    return deepcopy(TEST_DETAILS)


def test_get_clothes(temp_closet):
    browsing = browse.get_clothes()
    assert isinstance(browsing, list)
    assert len(browsing) + 1 > 1


def test_get_clothing_details(temp_closet):
    browse_dets = browse.get_clothing_details(browse.TEST_CLOTHING_NAME)
    assert isinstance(browse_dets, dict)


def test_add_wrong_name_type():
    with pytest.raises(TypeError):
        browse.add_clothing(7)


def test_add_wrong_details_type():
    with pytest.raises(TypeError):
        browse.add_clothing('a new clothing item', [])


def test_add_missing_field(details):
    del details[browse.SEASON]
    with pytest.raises(ValueError):
        browse.add_clothing('a new clothing item', details)


def test_add_clothing():
    details = {}
    for field in browse.REQUIRED_FLDS:
        details[field] = 2
    return details

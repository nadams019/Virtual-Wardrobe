"""
This module encapsulates details about our closet browsing page for the user.
"""
import db.db_connect as dbc

TEST_CATEGORY_NAME = 'Test Category'
CLOTHING = 'clothing'
SEASON = 'season'
OCCASION = 'occasion'
AESTHETIC = 'aesthetic'
RANDOM = 'random'

REQUIRED_FLDS = [SEASON, OCCASION, AESTHETIC, RANDOM]
closet = {TEST_CATEGORY_NAME: {SEASON: 'winter', OCCASION: 'formal',
                               AESTHETIC: 'vintage', RANDOM: 'False'},
          'handle': {SEASON: 'summer', OCCASION: 'casual',
                     AESTHETIC: 'preppy', RANDOM: 'True'},
          'dress': {SEASON: 'fall', OCCASION: 'school',
                    AESTHETIC: 'sporty', RANDOM: 'False'},
          'hat': {SEASON: 'spring', OCCASION: 'formal',
                  AESTHETIC: 'southern', RANDOM: 'True'}, },

CLOTHING_KEY = 'item'
CLOTHING_COLLECT = 'closet'

"""
Possible Category Types
Season: Winter, Spring, Summer, Fall
Occasion: Formal, Casual, Going-Out, Holiday
Aesthetic: Vintage, Casual, Gothic, Streetwear, Preppy
Random: Yes or No
"""


def clothing_exists(item_nm):
    """
    Returns whether or not a clothing item exists.
    """
    return get_clothing_details(item_nm) is not None


def get_clothing_dict():
    dbc.connect_db()
    return dbc.fetch_all_as_dict(CLOTHING_KEY, CLOTHING_COLLECT)


def get_clothes():
    dbc.connect_db()
    return dbc.fetch_all(CLOTHING_COLLECT)


def get_clothing_details(item_nm):
    dbc.connect_db()
    return dbc.fetch_one(CLOTHING_COLLECT, {CLOTHING: item_nm})


def add_clothing(item_nm):
    dbc.connect_db()
    if not isinstance(item_nm, dict):
        raise TypeError(f'Wrong type for clothing item: {type(item_nm)=}')
    for field in REQUIRED_FLDS:
        if field not in item_nm:
            raise ValueError(f'Required {field=} missing from clothing '
                             f'details.')
    return dbc.insert_one(CLOTHING_COLLECT, item_nm)


def del_clothing(item_nm):
    dbc.connect_db()
    dbc.del_one(CLOTHING_COLLECT, {CLOTHING: item_nm})


def main():
    print('Retrieving closet as a list:')
    closet = get_clothes()
    print(f'{closet=}')
    print('Getting closet as a dict:')
    closet = get_clothing_dict()
    print(f'{closet=}')
    print(f'{get_clothing_details(TEST_CATEGORY_NAME)=}')


if __name__ == '__main__':
    main()

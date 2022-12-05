"""
This module encapsulates details about our closet browsing page for the user.
"""
import db.db_connect as dbc

TEST_CATEGORY_NAME = 'Test Category'
CATEGORY = 'category'
CLOTHING = 'clothing'
SEASON = 'season'
OCCASION = 'occasion'
AESTHETIC = 'aesthetic'
RANDOM = 'random'

REQUIRED_FLDS = [CATEGORY, SEASON, OCCASION, AESTHETIC, RANDOM]
closet = {TEST_CATEGORY_NAME: {SEASON: 'winter', OCCASION: 'formal',
                               AESTHETIC: 'vintage', RANDOM: 'No'},
          'handle': {SEASON: 'summer', OCCASION: 'casual',
                     AESTHETIC: 'preppy', RANDOM: 'Yes'}}


CLOTHING_KEY = 'item'
CLOTHING_COLLECT = 'closet'


"""
Possible Category Types
Season: Winter, Spring, Summer, Fall
Occasion: Formal, Casual, Going-Out, Holiday
Aesthetic: Vintage, Casual, Gothic, Streetwear, Preppy
Random: Yes or No
"""


def clothing_exists(item):
    """
    Returns whether or not a clothing item exists.
    """
    return item in closet


def get_clothing_dict():
    dbc.connect_db()
    return dbc.fetch_all_as_dict(CLOTHING_KEY, CLOTHING_COLLECT)


def get_clothes():
    dbc.connect_db()
    return dbc.fetch_all(CLOTHING_COLLECT)


def get_clothing_details(item):
    return closet.get(item, None)


def add_clothing(item, details):
    if not isinstance(item, str):
        raise TypeError(f'Wrong type for clothing item: {type(item)=}')
    if not isinstance(details, dict):
        raise TypeError(f'Wrong type for clothing details: {type(details)=}')
    for field in REQUIRED_FLDS:
        if field not in details:
            raise ValueError(f'Required {field=} missing from clothing '
                             f'details.')
    closet[item] = details


def del_clothing(item):
    del closet[item]


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

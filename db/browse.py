"""
This module encapsulates details about our closet browsing page for the user.
"""

TEST_CLOTHING_NAME = 'Test clothing'
CLOTHING = 'clothing'
SEASON = 'season'
OCCASION = 'occasion'
AESTHETIC = 'aesthetic'
RANDOM = 'random'

REQUIRED_FLDS = [SEASON, OCCASION, AESTHETIC, RANDOM]
closet = {TEST_CLOTHING_NAME: {SEASON: 'winter', OCCASION: 'formal',
                               AESTHETIC: 'vintage', RANDOM: 'False'},
          'handle': {SEASON: 'summer', OCCASION: 'casual',
                     AESTHETIC: 'preppy', RANDOM: 'True'},
          'dress': {SEASON: 'fall', OCCASION: 'school',
                    AESTHETIC: 'sporty', RANDOM: 'False'},
          'hat': {SEASON: 'spring', OCCASION: 'formal',
                  AESTHETIC: 'southern', RANDOM: 'True'}, },

CLOTHING_KEY = 'name'
CLOTHING_COLLECT = 'closet'

"""
Possible Category Types
Season: Winter, Spring, Summer, Fall
Occasion: Formal, Casual, Going-Out, Holiday
Aesthetic: Vintage, Casual, Gothic, Street-wear, Preppy
Random: True or False
"""


def get_clothing_details(clothing):
    return closet.get(clothing, None)


def clothing_exists(name):
    """
    Returns a clothing item exists.
    """
    return name in closet


def get_clothing_dict():
    return closet


def get_clothes():
    return list(closet.keys())


def add_clothing(name, details):
    print("in add clothing")
    if not isinstance(name, str):
        raise TypeError(f'Wrong type for name: {type(name)=}')
    if not isinstance(details, dict):
        raise TypeError(f'Wrong type for details: {type(details)=}')
    for field in REQUIRED_FLDS:
        if field not in details:
            raise ValueError(f'Required {field=} missing from details.')
    closet[name] = details


def del_clothing(name):
    del closet[name]


def main():
    print('Retrieving closet as a list:')
    clothing = get_clothes()
    print(f'{clothing=}')
    print('Getting closet as a dict:')
    clothing = get_clothing_dict()
    print(f'{clothing=}')
    print(f'{get_clothing_details(TEST_CLOTHING_NAME)=}')


if __name__ == '__main__':
    main()

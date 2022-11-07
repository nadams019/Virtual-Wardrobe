"""
This module encapsulates details about our closet browsing page.
"""

TEST_CATEGORY_NAME = 'Test Category'
CATEGORY = 'category'
CLOTHING = 'clothing'
SEASON = 'season'
OCCASION = 'occasion'
AESTHETIC = 'aesthetic'
RANDOM = 'random'
BROWSE = 'browse'

# We expect the user database to change frequently:
# For now, we will consider EMAIL to be
# our mandatory fields.

REQUIRED_FLDS = [CATEGORY]
closet = {TEST_CATEGORY_NAME: {SEASON: 'winter', OCCASION: 'Prom', AESTHETIC: 'Classic', RANDOM: 'No'},
            'handle': {SEASON: 'summer', OCCASION: 'School', AESTHETIC: 'Emo', RANDOM: 'Yes'}}


def category_select(category):
    """
    :param category
    :return:
    """
    return


def clothing_exists(clothing):
    return clothing in closet


def get_clothes():
    return list(closet.keys())


def get_clothing_details(item):
    return closet.get(item, None)


def main():
    clothes = get_clothes()
    print(f'{clothes=}')
    print(f'{get_clothing_details(TEST_CATEGORY_NAME)=}')


if __name__ == '__main__':
    main()

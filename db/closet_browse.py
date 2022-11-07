"""
This module encapsulates details about our closet browsing page.
"""

TEST_CATEGORY_NAME = 'Test Category'
CATEGORY = 'category'
SEASON = 'season'
OCCASION = 'occasion'
AESTHETIC = 'aesthetic'
RANDOM = 'random'
BROWSE = 'browse'

# We expect the user database to change frequently:
# For now, we will consider EMAIL to be
# our mandatory fields.

REQUIRED_FLDS = [CATEGORY]
categories = {}
clothing = {TEST_CATEGORY_NAME: {SEASON: 'winter', OCCASION: 'Prom', AESTHETIC: 'Classic', RANDOM: 'No'},
            'handle': {SEASON: 'summer', OCCASION: 'School', AESTHETIC: 'Emo', RANDOM: 'Yes'}}


def category_select(category):
    """
    :param category
    :return:
    """
    return


def get_clothes():
    return


def get_clothing_details():
    return


def main():
    clothes = get_clothes()
    print(f'{clothing=}')
    print(f'{get_clothing_details(TEST_CATEGORY_NAME)=}')


if __name__ == '__main__':
    main()

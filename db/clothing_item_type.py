# This module encapsulates the details about the different dropdowns
import db.db_connect as dbc

TEST_OPTIONS = 'test options'
ITEM_TYPE = 'itemTypeButton'
SEASON = 'SeasonButton'
OCCASION = 'occasionButton'
AESTHETIC = 'aestheticButton'

REQUIRED_FIELDS = [ITEM_TYPE, SEASON, OCCASION, AESTHETIC]
char_types = {TEST_OPTIONS: {ITEM_TYPE: 'jeans',SEASON: 'winter', OCCASION: 'formal', AESTHETIC:'vintage'}, 
              {ITEM_TYPE: 'dresses',SEASON: 'summer', OCCASION: 'casual', AESTHETIC:'preppy'},
             {ITEM_TYPE: 'accessories',SEASON: 'fall', OCCASION: 'school', AESTHETIC:'sporty'},
             {ITEM_TYPE: 'Tops',SEASON: 'spring', OCCASION: 'formal', AESTHETIC:'southern'}

"""
def select_type(type_name, selections):
    select = Select(type_name)
    select.select_by_visible_text(selections)
"""


def select_values_from_dropdown(char_types, selections):
    print(len(char_types))
    for ele in char_types:
        print(ele.text)
        if ele.text == selections:
            ele.click()
            break


def add_char_type(type_name, selections):
    if char_type_exists(type_name):
        raise ValueError(f'Char type exists: {type_name=}')
    char_types[type_name] = selections


def del_char_type(type_name):
    if char_type_exists(type_name):
        del char_types[type_name]


def char_type_exists(type_name):
    return type_name in char_types


def get_char_types():
    return list(char_types.keys())


def get_char_type_details(char_type):
    return char_types.get(char_type, None)


def main():
    char_types = get_char_types()
    print(char_types)


if __name__ == '__main__':
    main()

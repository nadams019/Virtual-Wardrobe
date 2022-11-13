"""
This module encapsulates details about character type.
"""

WIZARD = 'Wizard'
WARRIOR = 'Warrior'
MAGE = 'Mage'

char_types = {WIZARD: {'health': 7, 'magic': 10},
              WARRIOR: {'health': 9, 'strength': 9},
              MAGE: {'health': 6}, }


def add_char_type(type_name, traits):
    if char_type_exists(type_name):
        raise ValueError(f'Char type exists: {type_name=}')
    char_types[type_name] = traits


def del_char_type(type_name):
    if char_type_exists(type_name):
        del char_types[type_name]


def char_type_exists(type_name):
    return type_name in char_types


def get_char_type_dict():
    """
    Returns a list of character types.
    """
    return char_types


def get_char_types():
    """
    Returns a list of character types.
    """
    return list(char_types.keys())


def get_char_type_details(char_type):
    return char_types.get(char_type, None)


def main():
    char_types = get_char_types()
    print(char_types)


if __name__ == '__main__':
    main()
"""
This module encapsulates details about aesthetics type.
"""

GRUNGE = 'Grunge'
ACADEMIA = 'Academia'
STREETWEAR = 'Street-wear'
COTTAGECORE = 'Cottage-core'
SOFTGIRL = 'Soft-girl'

aes_types = {GRUNGE: {'points': 1},
             ACADEMIA: {'points': 2},
             STREETWEAR: {'points': 3},
             COTTAGECORE: {'points': 4},
             SOFTGIRL: {'points': 5}, }


def add_aes_type(type_name, traits):
    if aes_type_exists(type_name):
        raise ValueError(f'Aes type exists: {type_name=}')
    aes_types[type_name] = traits


def del_aes_type(type_name):
    if aes_type_exists(type_name):
        del aes_types[type_name]


def aes_type_exists(type_name):
    return type_name in aes_types


def get_aes_type_dict():
    """
    Returns a list of aesthetic types.
    """
    return aes_types


def get_aes_types():
    """
    Returns a list of aesthetic types.
    """
    return list(aes_types.keys())


def get_aes_type_details(char_type):
    return aes_types.get(char_type, None)


def main():
    aes_types = get_aes_types()
    print(aes_types)


if __name__ == '__main__':
    main()

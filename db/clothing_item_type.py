# This module encapsulates the details about the different dropdowns

ITEM_TYPE = 'itemTypeButton'
SEASON = 'SeasonButton'
OCCASION = 'occasionButton'
AESTHETIC = 'aestheticButton'

char_types = {ITEM_TYPE: {'Tops', 'Bottoms', 'Dresses', 'Accessories',
                          'Jackets'},
              SEASON: {'Fall', 'Winter', 'Summer', 'Spring'},
              OCCASION: {'Casual', 'Formal', 'Semi-formal',
                         'Business', 'Party'},
              AESTHETIC: {'Grunge', 'Academia', 'Streetwear', 'Cottagecore',
                          'Indie', 'Soft girl'},
              }

def select_type(type_name, selections):
    select = Select(type_name)
    select.select_by_visible_text(selections)
    
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

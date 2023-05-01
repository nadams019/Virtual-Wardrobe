import os
import pytest

closet_items = []

ITEM_TYPES = ['Shirt', 'Pants', 'Skirt', 'Dress', 'Jacket', 'Coat', 'Sweater', 'Blouse',
    'T-Shirt', 'Tank Top', 'Shorts', 'Suit', 'Vest', 'Scarf', 'Hat', 'Gloves',
    'Shoes', 'Boots', 'Sandals', 'Sneakers', 'Heels', 'Flats']
SEASONS = [
    'Spring', 'Summer', 'Fall', 'Winter'
]
OCCASIONS = [
    'Casual', 'Formal', 'Business', 'Athletic', 'Evening', 'Wedding'
]
AESTHETICS = [
    'Classic', 'Vintage', 'Minimalist', 'Bohemian', 'Gothic', 'Romantic', 'Preppy',
    'Trendy', 'Sporty', 'Artsy', 'Punk', 'Girly'
]

REQUIRED_FIELDS = ['item_type', 'season', 'occasion', 'aesthetic']


@pytest.fixture(scope='function')
def validate_item(item):
    """
    Validate the given item has all required fields.
    """
    for field in REQUIRED_FIELDS:
        if field not in item:
            raise ValueError(f"Item is missing required field '{field}'")
def add_item(item):
    """
    Add a clothing item to the closet.
    """
    validate_item(item)
    closet_items.append(item)

def delete_item(item):
    """
    delete a clothing item from the closet.
    """
    closet_items.remove(item)

def get_items():
    """
    Retrieve all clothing items in the closet.
    """
    return closet_items

def filter_items(item_type=None, season=None, occasion=None, aesthetic=None):
    """
    Filter the closet items by any combination of type, season, occasion, and aesthetic.
    """
    filtered_items = closet_items

    if item_type:
        filtered_items = [item for item in filtered_items if item.get('item_type') == item_type]

    if season:
        filtered_items = [item for item in filtered_items if item.get('season') == season]

    if occasion:
        filtered_items = [item for item in filtered_items if item.get('occasion') == occasion]

    if aesthetic:
        filtered_items = [item for item in filtered_items if item.get('aesthetic') == aesthetic]

    return filtered_items




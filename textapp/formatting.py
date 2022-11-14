

"""
This file takes care of our text formatting for the textapp package.
"""

import os
# import colorama  Do we really need this?

# light means light screen, so dark text!
LIGHT = "light"
DARK = "dark"
GREEN = "green"
RED = "red"
BLACK = "black"
WHITE = "white"
MAGENTA = "magenta"
CYAN = "cyan"
YELLOW = "yellow"
BOLD = "bold"

TEXT_MENU_MODE = "TEXT_MENU_MODE"

DEF_SEP_LEN = 60
DEF_SEP_CHAR = '*'

color_scheme = os.getenv(TEXT_MENU_MODE, DARK)  # some default!

HAS_TERMCOLOR = True
try:
    from termcolor import colored # noqa
except ImportError:
    HAS_TERMCOLOR = False


SEPERATOR = "SEPERATOR"
TITLE = "TITLE"
TEXT = "TEXT"
MENU_CHOICE = "MENU_CHOICE"

DARK_SCHEME = {
    SEPERATOR: {'color': CYAN, 'attrs': None},
    TITLE: {'color': YELLOW, 'attrs': [BOLD]},
    TEXT: {'color': WHITE, 'attrs': None},
    MENU_CHOICE: {'color': CYAN, 'attrs': None},
}

LIGHT_SCHEME = {
    SEPERATOR: {'color': RED, 'attrs': None},
    TITLE: {'color': MAGENTA, 'attrs': [BOLD]},
    TEXT: {'color': BLACK, 'attrs': None},
    MENU_CHOICE: {'color': RED, 'attrs': None},
}

color_map = DARK_SCHEME if color_scheme == DARK else LIGHT_SCHEME


def fmt_text(text, elem=TEXT):
    if HAS_TERMCOLOR:
        text = colored(text, color_map[elem]['color'],
                       attrs=color_map[elem]['attrs'])
    return text


def menu_choice(text):
    return fmt_text(text, elem=MENU_CHOICE)


def sep(in_menu=False, char=DEF_SEP_CHAR, length=DEF_SEP_LEN):
    return fmt_text(char*length, elem=SEPERATOR)


def title(text, in_menu=False, sep_char=DEF_SEP_CHAR, sep_length=DEF_SEP_LEN):
    seper = f"{sep(in_menu, char=DEF_SEP_CHAR, length=DEF_SEP_LEN)}"
    text = fmt_text(text, elem=TITLE)
    return f"\n{seper}\n{text}\n{seper}\n"


def main():
    print(title("Does this title get printed?"))


if __name__ == "__main__":
    main()
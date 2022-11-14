"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""
from http import HTTPStatus

from flask import Flask, request
from flask_restx import Resource, Api, fields, Namespace
import werkzeug.exceptions as wz

import db.char_types as ctyp
import db.quiz as qz
import db.games as gm
import db.users as usr

# import db.closet_browse as brwse

app = Flask(__name__)
api = Api(app)

CHAR_TYPES_NS = 'character_types'
GAMES_NS = 'games'
USERS_NS = 'users'
CLOSETBROWSE_NS = 'closet_broswe'

char_types = Namespace(CHAR_TYPES_NS, 'Character Types')
api.add_namespace(char_types)
games = Namespace(GAMES_NS, 'Games')
api.add_namespace(games)
users = Namespace(USERS_NS, 'Users')
api.add_namespace(users)
closet_browse = Namespace(CLOSETBROWSE_NS, 'Closet Browse')
api.add_namespace(closet_browse)

LIST = 'list'
DICT = 'dict'
DETAILS = 'details'
ADD = 'add'
MAIN_MENU = '/main_menu'
MAIN_MENU_NM = 'Main Menu'
HELLO = '/hello'
MESSAGE = 'message'
CHAR_TYPE_DICT = f'/{DICT}'
CHAR_TYPE_DICT_W_NS = f'{CHAR_TYPES_NS}/{DICT}'
CHAR_TYPE_DICT_NM = f'{CHAR_TYPES_NS}_dict'
CHAR_TYPE_LIST = f'/{LIST}'
CHAR_TYPE_LIST_W_NS = f'{CHAR_TYPES_NS}/{LIST}'
CHAR_TYPE_LIST_NM = f'{CHAR_TYPES_NS}_list'
CHAR_TYPE_DETAILS = f'/{DETAILS}'
CHAR_TYPE_DETAILS_W_NS = f'{CHAR_TYPES_NS}/{DETAILS}'
GAME_DICT = f'/{DICT}'
GAME_DICT_W_NS = f'{GAMES_NS}/{DICT}'
GAME_DETAILS = f'/{DETAILS}'
GAME_DETAILS_W_NS = f'{GAMES_NS}/{DETAILS}'
GAME_ADD = f'/{GAMES_NS}/{ADD}'
USER_DICT = f'/{DICT}'
USER_DICT_W_NS = f'{USERS_NS}/{DICT}'
USER_DICT_NM = f'{USERS_NS}_dict'
USER_LIST = f'/{LIST}'
USER_LIST_W_NS = f'{USERS_NS}/{LIST}'
USER_LIST_NM = f'{USERS_NS}_list'
USER_DETAILS = f'/{USERS_NS}/{DETAILS}'
USER_ADD = f'/{USERS_NS}/{ADD}'
CLOSETBROWSE_DICT = f'/{DICT}'
CLOSETBROWSE_DICT_W_NS = f'{CLOSETBROWSE_NS}/{DICT}'
CLOSETBROWSE_DICT_NM = f'{CLOSETBROWSE_NS}_dict'
CLOSETBROWSE_LIST = f'/{LIST}'
CLOSETBROWSE_LIST_W_NS = f'{CLOSETBROWSE_NS}/{LIST}'
CLOSETBROWSE_LIST_NM = f'{CLOSETBROWSE_NS}_list'
CLOSETBROWSE_DETAILS = f'/{CLOSETBROWSE_NS}/{DETAILS}'
CLOSETBROWSE_ADD = f'/{CLOSETBROWSE_NS}/{ADD}'


@api.route(HELLO)
class HelloWorld(Resource):
    """
    The purpose of the HelloWorld class is to have a simple test to see if the
    app is working at all.
    """

    def get(self):
        """
        A trivial endpoint to see if the server is running.
        It just answers with "hello world."
        """
        return {MESSAGE: 'hello world'}


@api.route(MAIN_MENU)
class MainMenu(Resource):
    """
    This will deliver our main menu.
    """

    def get(self):
        """
        Gets the main game menu.
        """
        return {'Title': MAIN_MENU_NM,
                'Default': 2,
                'Choices': {
                    '1': {'url': f'/{CHAR_TYPE_DICT_W_NS}', 'method': 'get',
                          'text': 'List Character Types'},
                    '2': {'url': f'/{GAME_DICT_W_NS}',
                          'method': 'get', 'text': 'List Active Games'},
                    '3': {'url': f'/{USER_DICT_W_NS}',
                          'method': 'get', 'text': 'List Users'},
                    '4': {'url': f' / {CLOSETBROWSE_DICT_W_NS}',
                          'method': 'get', 'text': 'List Users'},
                    'X': {'text': 'Exit'},
                }}


@char_types.route(CHAR_TYPE_LIST)
class CharacterTypeList(Resource):
    """
    This will get a list of character types.
    """

    def get(self):
        """
        Returns a list of character types.
        """
        return {CHAR_TYPE_LIST_NM: ctyp.get_char_types()}


@char_types.route(CHAR_TYPE_DICT)
class CharacterTypeDict(Resource):
    """
    This will get a list of character types.
    """

    def get(self):
        """
        Returns a list of character types.
        """
        return {'Data': ctyp.get_char_type_dict(),
                'Type': 'Data',
                'Title': 'Character Types'}


@char_types.route(f'{CHAR_TYPE_DETAILS}/<char_type>')
class CharacterTypeDetails(Resource):
    """
    This will return details on a character type.
    """

    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self, char_type):
        """
        This will return details on a character type.
        """
        ct = ctyp.get_char_type_details(char_type)
        if ct is not None:
            return {char_type: ctyp.get_char_type_details(char_type)}
        else:
            raise wz.NotFound(f'{char_type} not found.')

####****

@games.route(f'{GAME_DETAILS}/<game>')
class GameDetails(Resource):
    """
    This will get details on a game.
    """

    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self, game):
        """
        Returns a list of character types.
        """
        ct = gm.get_game_details(game)
        if ct is not None:
            return {game: gm.get_game_details(game)}
        else:
            raise wz.NotFound(f'{game} not found.')


Aesthetic_quiz_fields = api.model('Start Quiz', {
    qz.NAME: fields.String,
    
})

@api.route(GAME_ADD)
class AddGame(Resource):
    """
    Add a game.
    """

    @api.expect(game_fields)
    def post(self):
        """
        Add a game.
        """
        print(f'{request.json=}')
        name = request.json[gm.NAME]
        del request.json[gm.NAME]
        gm.add_game(name, request.json)


@users.route(USER_DICT)
class UserDict(Resource):
    """
    This will get a list of currrent users.
    """

    def get(self):
        """
        Returns a list of current users.
        """
        return {'Data': usr.get_users_dict(),
                'Type': 'Data',
                'Title': 'Active Users'}


@users.route(USER_LIST)
class UserList(Resource):
    """
    This will get a list of currrent users.
    """

    def get(self):
        """
        Returns a list of current users.
        """
        return {USER_LIST_NM: usr.get_users()}


user_fields = api.model('NewUser', {
    usr.NAME: fields.String,
    usr.EMAIL: fields.String,
    usr.FULL_NAME: fields.String,
})


@api.route(USER_ADD)
class AddUser(Resource):
    """
    Add a user.
    """

    @api.expect(user_fields)
    def post(self):
        """
        Add a user.
        """
        print(f'{request.json=}')
        name = request.json[usr.NAME]
        del request.json[usr.NAME]
        usr.add_user(name, request.json)


@api.route('/endpoints')
class Endpoints(Resource):
    """
    This class will serve as live, fetchable documentation of what endpoints
    are available in the system.
    """

    def get(self):
        """
        The `get()` method will return a list of available endpoints.
        """
        endpoints = ''
        # sorted(rule.rule for rule in api.app.url_map.iter_rules())
        return {"Available endpoints": endpoints}

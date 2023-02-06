"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""
from http import HTTPStatus
from flask import Flask, request
from flask_restx import Resource, Api, fields, Namespace
import werkzeug.exceptions as wz
import db.users as usr
import db.closet_browse as brwse
import db.browse as br
import db.contacts as cnts
import db.aesthetics_types as atyp

app = Flask(__name__)
api = Api(app)

LOGIN_NS = 'login'
USERS_NS = 'users'
CLOSET_NS = 'closet'
BROWSE_NS = 'browse'
CONTACTS_NS = 'contacts'
AES_TYPES_NS = 'aesthetics_types'


login = Namespace(LOGIN_NS, 'Login')
api.add_namespace(login)
users = Namespace(USERS_NS, 'Users')
api.add_namespace(users)
closet = Namespace(CLOSET_NS, 'Closet')
api.add_namespace(closet)
browse = Namespace(BROWSE_NS, 'Browse')
api.add_namespace(browse)
contacts = Namespace(CONTACTS_NS, 'Contacts')
api.add_namespace(contacts)
aes_types = Namespace(AES_TYPES_NS, 'Aesthetics Types')
api.add_namespace(aes_types)

LOGIN = '/login'
LIST = 'list'
DICT = 'dict'
DETAILS = 'details'
ADD = 'add'
MAIN_MENU = '/main_menu'
MAIN_MENU_NM = 'Main Menu'
HELLO = '/hello'
MESSAGE = 'message'


USER_DICT = f'/{DICT}'
USER_DICT_W_NS = f'{USERS_NS}/{DICT}'
USER_DICT_NM = f'{USERS_NS}_dict'
USER_LIST = f'/{LIST}'
USER_LIST_W_NS = f'{USERS_NS}/{LIST}'
USER_LIST_NM = f'{USERS_NS}_list'
USER_DETAILS = f'/{USERS_NS}/{DETAILS}'
USER_ADD = f'/{USERS_NS}/{ADD}'


BROWSE_DICT = f'/{DICT}'
BROWSE_DICT_W_NS = f'{BROWSE_NS}/{DICT}'
BROWSE_DETAILS = f'/{DETAILS}'
BROWSE_DETAILS_W_NS = f'{BROWSE_NS}/{DETAILS}'
BROWSE_ADD = f'/{BROWSE_NS}/{ADD}'


CLOSET_LIST = f'{LIST}'
CLOSET_LIST_NM = f'{CLOSET_NS}_list'
CLOSET_LIST_W_NS = f'{CLOSET_NS}/{LIST}'
CLOSET_DICT_NM = f'{CLOSET_NS}_dict'
CLOSET_DICT = f'/{DICT}'
CLOSET_DICT_W_NS = f'{CLOSET_NS}/{DICT}'
CLOSET_DETAILS = f'/{DETAILS}'
CLOSET_DETAILS_W_NS = f'{CLOSET_NS}/{DETAILS}'
CLOSET_ADD = f'/{CLOSET_NS}/{ADD}'


CONTACTS_DICT = f'/{DICT}'
CONTACTS_DICT_W_NS = f'{CONTACTS_NS}/{DICT}'
CONTACTS_DICT_NM = f'{CONTACTS_NS}_dict'
CONTACTS_LIST = f'/{LIST}'
CONTACTS_LIST_W_NS = f'{CONTACTS_NS}/{LIST}'
CONTACTS_LIST_NM = f'{CONTACTS_NS}_list'
CONTACTS_DETAILS = f'/{CONTACTS_NS}/{DETAILS}'
CONTACTS_ADD = f'/{CONTACTS_NS}/{ADD}'


AES_TYPE_DICT = f'/{DICT}'
AES_TYPE_DICT_W_NS = f'{AES_TYPES_NS}/{DICT}'
AES_TYPE_DICT_NM = f'{AES_TYPES_NS}_dict'
AES_TYPE_LIST = f'/{LIST}'
AES_TYPE_LIST_W_NS = f'{AES_TYPES_NS}/{LIST}'
AES_TYPE_LIST_NM = f'{AES_TYPES_NS}_list'
AES_TYPE_DETAILS = f'/{DETAILS}'
AES_TYPE_DETAILS_W_NS = f'{AES_TYPES_NS}/{DETAILS}'


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
                    '1': {'url': f'/{LOGIN_NS}',
                          'method': 'post', 'text': 'Login'},
                    '2': {'url': f'/{USER_DICT_W_NS}',
                          'method': 'get', 'text': 'List Users'},
                    '3': {'url': f' / {CLOSET_DICT_W_NS}',
                          'method': 'get', 'text': 'List Clothes '
                                                   'in Closet'},
                    '4': {'url': f' / {CONTACTS_DICT_W_NS}',
                          'method': 'get', 'text': 'List Contacts'},
                    '5': {'url': f' / {AES_TYPE_DICT_W_NS}',
                          'method': 'get', 'text': 'List Aesthetic Types'},
                    'X': {'text': 'Exit'},
                }}


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
    This will get a list of current users.
    """
    def get(self):
        """
        Returns a list of current users.
        """
        return {USER_LIST_NM: usr.get_users()}


user_fields = api.model('NewUser', {
    usr.USERNAME: fields.String,
    usr.PASSWORD: fields.String,
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
        name = request.json[usr.USERNAME]
        del request.json[usr.USERNAME]
        usr.add_user(name, request.json)


@browse.route(BROWSE_DICT)
class BrowseList(Resource):
    """
    This will get a list of current clothing items.
    """
    def get(self):
        """
        Returns a list of current clothing items.
        """
        return {'Data': br.get_clothing_dict(),
                'Type': 'Data',
                'Title': 'Available Clothing'}


@browse.route(f'{BROWSE_DETAILS}/<browse>')
class BrowseDetails(Resource):
    """
    This will get details on a clothing.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self, browse_dets):
        """
        Returns a list of browse details.
        """
        ct = br.get_clothing_details(browse_dets)
        if ct is not None:
            return {browse: br.get_clothing_details(browse_dets)}
        else:
            raise wz.NotFound(f'{browse} not found.')


browse_fields = api.model('NewClothing', {
    br.CLOTHING: fields.String,
    br.SEASON: fields.String,
    br.OCCASION: fields.String,
    br.AESTHETIC: fields.String,
    br.RANDOM: fields.String,
})


@api.route(BROWSE_ADD)
class AddClothing(Resource):
    """
    Add a clothing item.
    """
    @api.expect(browse_fields)
    def post(self):
        """
        Add a clothing item.
        """
        print(f'{request.json=}')
        name = request.json[br.CLOTHING]
        del request.json[br.CLOTHING]
        br.add_clothing(name, request.json)


@closet.route(CLOSET_LIST)
class ClosetList(Resource):
    def get(self):
        """
        Returns a list of available clothing items in the virtual wardrobe
        """
        return {'Data': brwse.get_clothes(),
                'Type': 'Data',
                'Title': 'Available Clothes'}


@closet.route(f'{CLOSET_DETAILS}/<closet>')
class ClosetDetails(Resource):
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self, closet_nm):
        """
        This will give details on a clothing item.
        """
        ct = brwse.get_clothing_details(closet_nm)
        if ct is not None:
            return {closet: brwse.get_clothing_details(closet_nm)}
        else:
            raise wz.NotFound(f'{closet_nm} not found.')


closet_fields = api.model('NewItem', {
    brwse.CLOTHING: fields.String,
    brwse.SEASON: fields.String,
    brwse.OCCASION: fields.String,
    brwse.AESTHETIC: fields.String,
    brwse.RANDOM: fields.Boolean,
})


@api.route(CLOSET_ADD)
class AddItem(Resource):
    @api.expect(closet_fields)
    def post(self):
        """
        Adds a clothing item to virtual wardrobe.
        """
        print(f'{request.json=}')
        name = request.json[brwse.CLOTHING]
        del request.json[brwse.CLOTHING]
        brwse.add_clothing(name, request.json)


@contacts.route(CONTACTS_DICT)
class ContactDict(Resource):
    """
    This will get a list of currrent contact.
    """
    def get(self):
        """
        Returns a list of current contacts.
        """
        return {'Data': cnts.get_contacts_dict(),
                'Type': 'Data',
                'Title': 'Contact Requests'}


@contacts.route(CONTACTS_LIST)
class ContactList(Resource):
    """
    This will get a list of currrent users.
    """
    def get(self):
        """
        Returns a list of current users.
        """
        return {CONTACTS_LIST_NM: cnts.get_contacts()}


contacts_fields = api.model('NewContact', {
    cnts.EMAIL: fields.String,
    cnts.FULL_NAME: fields.String,
    cnts.REQUEST: fields.String
})


@api.route(CONTACTS_ADD)
class AddContacts(Resource):
    """
    Add a user.
    """
    @api.expect(user_fields)
    def post(self):
        """
        Add a user.
        """
        print(f'{request.json}')
        name = request.json[cnts.FULL_NAME]
        del request.json[cnts.FULL_NAME]
        cnts.add_contact(name, request.json)


@aes_types.route(AES_TYPE_LIST)
class AestheticTypeList(Resource):
    """
    This will get a list of aesthetic types.
    """
    def get(self):
        """
        Returns a list of aesthetic types.
        """
        return {AES_TYPE_LIST_NM: atyp.get_aes_types()}


@aes_types.route(AES_TYPE_DICT)
class AestheticTypeDict(Resource):
    """
    This will get a list of aesthetic types.
    """
    def get(self):
        """
        Returns a list of aesthetic types.
        """
        return {'Data': atyp.get_aes_type_dict(),
                'Type': 'Data',
                'Title': 'Aesthetics Types'}


@aes_types.route(f'{AES_TYPE_DETAILS}/<aes_type>')
class AestheticTypeDetails(Resource):
    """
    This will return details on a aesthetic type.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self, aes_type):
        """
        This will return details on an aesthetic type.
        """
        atype = atyp.get_aes_type_details(aes_type)
        if atype is not None:
            return {aes_type: atyp.get_aes_type_details(aes_type)}
        else:
            raise wz.NotFound(f'{aes_type} not found.')


# @login.route(LOGIN, methods=['GET', 'POST'])
# def login():
#     """
#     The login page for the closet.
#     """
#     error = None
#     if request.method == "POST":
#         email = request.form['email']
#         full_name = request.form['full name']
#         username = request.form['username']
#         password = request.form['password']
#
#         try:
#             user_found = usr.user_exists(email, full_name,
#             username, password)
#         except Exception as error:
#             print(f"Error logging in: {error}")
#
#         if user_found is True:
#             session['email'] = email
#             session['full_name'] = full_name
#             return redirect(url_for(MAIN_MENU))
#
#         else:
#             error = "Login failed"
#             return render_template('login.html', error=error)


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

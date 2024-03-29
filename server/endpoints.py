"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""
from http import HTTPStatus
from flask_cors import CORS
from flask import Flask, render_template, request, redirect, url_for, \
    session, jsonify
from flask_restx import Resource, Api, fields, Namespace
import werkzeug.exceptions as wz
import db.users as usr
import db.closet_browse as brwse
import db.browse as br
import db.contacts as cnts
import db.aesthetics_types as atyp
import secrets

AUTH_KEY = 'Auth-Key'
SWAG_AUTH_TYPE_FIELD = 'type'
SWAG_AUTH_TYPE = 'apiKey'
SWAG_AUTH_LOC_FIELD = 'in'
SWAG_AUTH_LOC = 'in'
SWAG_AUTH_NM_FIELD = 'name'
authorizations = {
    AUTH_KEY: {
        SWAG_AUTH_TYPE_FIELD: SWAG_AUTH_TYPE,
        SWAG_AUTH_LOC_FIELD: SWAG_AUTH_LOC,
        SWAG_AUTH_NM_FIELD: AUTH_KEY
    }
}
app = Flask(__name__)
CORS(app)
api = Api(app, authorizations=authorizations)
app.secret_key = secrets.token_hex(16)

LOGIN_NS = 'login'
USERS_NS = 'users'
CLOSET_NS = 'closet'
BROWSE_NS = 'browse'
CONTACTS_NS = 'contacts'
AES_TYPES_NS = 'aesthetics_types'
UPLOAD_NS = 'upload'
OPTIONS = '/options'
CLOTHING_ITEM_TYPE_NS = 'clothing_item_type'
SEASON_NS = 'season'
OCCASION_NS = 'occasion'
AESTHETIC_NS = 'aesthetic'

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
upload = Namespace(UPLOAD_NS, 'Upload')
api.add_namespace(upload)

LOGIN = '/login'
LIST = 'list'
DICT = 'dict'
DETAILS = 'details'
ADD = 'add'
MAIN_MENU = '/main_menu'
MAIN_MENU_NM = 'Main Menu'
HELLO = '/hello'
MESSAGE = 'message'
OPTIONS_NM = "option"
UPLOAD = '/upload'

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
CONTACTS_DETAILS_W_NS = f'{CONTACTS_NS}/{DETAILS}'
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
        return {MESSAGE: 'Hello world'}


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


@api.route(OPTIONS)
class OptionsMenu(Resource):
    """
    This will deliver the option menu for seeing details in the closet
    """

    def get(self):
        return {'Title': OPTIONS_NM,
                'Default': 2,
                'Choices': {
                    '1': {'url': f'/{CLOTHING_ITEM_TYPE_NS}',
                          'method': 'post', 'text': 'Item in closet'},
                    '2': {'url': f'/{SEASON_NS}',
                          'method': 'get', 'text': 'List the season'},
                    '3': {'url': f' / {OCCASION_NS}',
                          'method': 'get', 'text': 'List the occasion'},
                    '4': {'url': f' / {AESTHETIC_NS}',
                          'method': 'get', 'text': 'List the aesthetic'},
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
        '''
        return {'Data': brwse.get_clothes(),
                'Type': 'Data',
                'Title': 'Available Clothes'}
        '''
        return {CLOSET_LIST_NM: brwse.get_clothes()}


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


@app.route('/home_page')
def home_page():
    return render_template('home_page.html')


@app.route(LOGIN, methods=['POST'])
def login():
    """
    Code for the login page.
    """
    error = None
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if username == 'sample_user' and password == 'abcde123':
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('home_page'))

        else:
            error = "Login failed"

    return render_template('login_page.html', error=error)


@app.route('/upload_closet')
def upload_closet_nav():
    return render_template('pages/uploadCloset.html')


@app.route(UPLOAD, methods=['POST'])
def upload_closet():
    if request.method == "POST":
        item_type = request.form['item_type']
        aesthetic = request.form['aesthetic']
        occasion = request.form['occasion']
        season = request.form['season']
        if item_type and aesthetic and occasion and season:
            return jsonify({'message': 'Clothing item uploaded successfully!',
                            'success': True})
        else:
            # Return an error message
            return jsonify({'success': False,
                            'message': 'All fields are required!'})
    else:
        return upload_closet_nav

    # return render_template('UploadCloset.html', error=error)


'''
UPLOAD_FOLDER = '/path/to/upload/folder'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the post request has the file part
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    # If the user does not select a file, browser also
    # submits an empty part without filename
    if file.filename == '':
        return 'No selected file'

    # Process the uploaded file
    # You can save it to the server or do any other operations

    return 'File uploaded successfully'


@upload.route('/closet/<int:closet_id>/upload', methods=['POST'])
class ClosetUpload(Resource):
    """
   This endpoint allows users to upload images for their closet items.
   """

    def post(self, closet_id):
        if 'file' not in request.files:
            return {'message': 'No file part'}, 400
        file = request.files['file']
        if file.filename == '':
            return {'message': 'No selected file'}, 400
        if not allowed_file(file.filename):
            return {'message': 'Invalid file type'}, 400
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        # add filename to database for closet item with closet_id
        return {'message': 'File uploaded successfully'}, 201
'''


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


if __name__ == '__main__':
    app.run()

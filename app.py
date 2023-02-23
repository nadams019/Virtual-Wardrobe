from flask import Flask, Blueprint
import db.users as usr
import db.closet_browse as brwse
import argparse

app = Flask(__name__)
USERS_NS = 'users'
CLOSET_BROWSE_NS = 'closet_browse'

closet_browse_bp = Blueprint('closet_browse', __name__, url_prefix='/closet_browse')

LIST = 'list'
DETAILS = 'details'
ADD = 'add'
MAIN_MENU = '/main_menu'
MAIN_MENU_NM = 'Main Menu'
HELLO = '/hello'
MESSAGE = 'message'
CLOSET_LIST = f'/{CLOSET_BROWSE_NS}/{LIST}'
CLOSET_LIST_NM = f'{CLOSET_BROWSE_NS}_list'
CLOSET_DETAILS = f'/{CLOSET_BROWSE_NS}/{DETAILS}'
CLOSET_ADD = f'/{CLOSET_BROWSE_NS}/{ADD}'
USER_LIST = f'/{USERS_NS}/{LIST}'
USER_LIST_NM = f'/{USERS_NS}_list'
USER_DETAILS = f'/{USERS_NS}/{DETAILS}'
USER_ADD = f'/{USERS_NS}/{ADD}'


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


#@app.route(HELLO)
#class HelloWorld(Resource):
    #def get(self):
        #"""
        #A trivial endpoint to see if the server is working properly.
        #It just answers with hello world.
        #"""
        #return {MESSAGE: 'hello world'}


@app.route(MAIN_MENU)
class MainMenu(Resource):
    def get(self):
        """
        Gets the main menu
        """
        return {MAIN_MENU_NM: {'the': 'menu'}}


if __name__ == '__main__':
    ''' To run flask: flask run -h localhost -p 8000'''
    app.run('http://127.0.0.1:8000')

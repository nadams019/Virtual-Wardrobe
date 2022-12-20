from flask import Flask
import db.users as usr
import db.closet_browse as brwse

app = Flask(__name__)
USERS_NS = 'users'
CLOSET_NS = 'closet'

#closet_browse = Namespace(CLOSET_NS, 'Closet Browse')
#app.add_namespace(closet_browse)

LIST = 'list'
DETAILS = 'details'
ADD = 'add'
MAIN_MENU = '/main_menu'
MAIN_MENU_NM = 'Main Menu'
HELLO = '/hello'
MESSAGE = 'message'
CLOSET_LIST = f'/{CLOSET_NS}/{LIST}'
CLOSET_LIST_NM = f'{CLOSET_NS}_list'
CLOSET_DETAILS = f'/{CLOSET_NS}/{DETAILS}'
CLOSET_ADD = f'/{CLOSET_NS}/{ADD}'
USER_LIST = f'/{USERS_NS}/{LIST}'
USER_LIST_NM = f'/{USERS_NS}_list'
USER_DETAILS = f'/{USERS_NS}/{DETAILS}'
USER_ADD = f'/{USERS_NS}/{ADD}'


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route(HELLO)
class HelloWorld(Resource):
    def get(self):
        """
        A trivial endpoint to see if the server is working properly.
        It just answers with hello world.
        """
        return {MESSAGE: 'hello world'}


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

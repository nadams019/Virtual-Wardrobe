from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/main_menu')
def menu():
    return


if __name__ == '__main__':
    ''' To run flask: flask run -h localhost -p 8000'''
    app.run('http://127.0.0.1:8000')

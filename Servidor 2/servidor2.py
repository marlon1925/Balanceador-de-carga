from flask import flask

servidor2 = Flask(__name__)

@servidor2.route('/')

def hola():
    return "Hola desde servidor 1"

if __name__ == '__main__':
    servidor2.run(host='0.0.0.0')

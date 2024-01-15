from flask import flask

servidor4 = Flask(__name__)

@servidor4.route('/')

def hola():
    return "Hola desde servidor 1"

if __name__ == '__main__':
    servidor4.run(host='0.0.0.0')

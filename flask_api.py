import logging
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route('/')
def my_api():
    return 'This is my first API'


@app.route('/calculate')
def calculate():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    op = request.args.get('op')

    if a is None or b is None or op is None:
        return jsonify({'error': 'Provide integers a, b and an operator'}), 400

    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        if b == 0:
            logger.error("Division by zero attempted: a=%s", a)
            return jsonify({'error': 'Cannot divide by zero'}), 400
        result = a / b
    else:
        return jsonify({'error': 'Invalid operation'}), 400

    return jsonify({'first': a, 'second': b, 'operation': op, 'result': result})


if __name__ == '__main__':
    app.run()
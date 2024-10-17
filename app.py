from flask import Flask, jsonify

app = Flask(__name__)

todos = ['eat', 'sleep', 'code']


@app.route('/')
def index():
    return "Todo List API is running!"


@app.route('/todos', methods=['GET'])
def getTodos():
    return jsonify(todos), 200


if __name__ == '__main__':
    app.run(debug=True)

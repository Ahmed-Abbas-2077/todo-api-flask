from flask import Flask, jsonify

app = Flask(__name__)

todos = []
currId = 1


@app.route('/')
def index():
    return "Todo List API is running!"


@app.route('/todos', methods=['GET'])
def getTodos():
    return jsonify(todos), 200


@app.route('/todos', methods=['POST'])
def createTodo():
    global currId
    if not request.json or 'title' not in request.json:
        abort(400, description="You gotta have a title for your todo!")
    todo = {
        'id': currId,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    todos.append(todo)
    currId += 1
    return jsonify(todo), 201


@app.route('/todos/<int:todo_id>', methods=['GET'])
def getTodo(todo_id):
    if todo_id < len(todos):
        return jsonify(todos[todo_id]), 200
    else:
        abort(404, description="Todo not found")


if __name__ == '__main__':
    app.run(debug=True)

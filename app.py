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
    global todos
    if todo_id < len(todos):
        return jsonify(todos[todo_id]), 200
    else:
        abort(404, description="Todo not found")


@app.route('/todos/<int:todo_id>', methods=['PUT'])
def updateTodo(todo_id):
    global todos
    if todo_id >= len(todos):
        abort(404, description="Todo not found")
    if not request.json:
        abort(400, description="Invalid input")

    todo = todos[todo_id]
    title = request.json.get('title', todo['title'])
    description = request.json.get('description', todo['description'])
    done = request.json.get('done', todo['done'])

    # check data types
    if not isinstance(title, str) or not isinstance(description, str) or not isinstance(done, bool):
        abort(400, description="Invalid data types")

    # update the todo
    todo.update({
        'title': title,
        'description': description,
        'done': done
    })
    return jsonify(todo), 200


@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def deleteTodo(todo_id):
    global todos
    if todo_id >= len(todos):
        abort(404, description="Todo not found")
    todo = todos[todo_id]
    todos = [item for item in todos if item['id'] != todo_id]
    return jsonify({'result': True}), 200


if __name__ == '__main__':
    app.run(debug=True)

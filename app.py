from flask import Flask, request, jsonify
from uuid import uuid4
from threading import Thread
import time
from call_gpt import generate_text

app = Flask(__name__)

# In-memory storage for tasks
tasks = {}

# Helper function to perform long-running tasks
def run_task(task_id, task_type, params):
    if task_type == 'sum':
        time.sleep(2)  # simulate a long-running task
        tasks[task_id]['result'] = sum(params)
    elif task_type == 'gpt':
        tasks[task_id]['result'] = generate_text(params[0])
    elif task_type == 'reverse':
        tasks[task_id]['result'] = params[0][::-1]

    tasks[task_id]['status'] = 'done'


@app.route('/task', methods=['POST'])
def add_task():
    task_type = request.json['type']
    params = request.json['params']
    
    task_id = str(uuid4())
    tasks[task_id] = {'status': 'running'}

    # Run the task in a separate thread so we don't block the response
    Thread(target=run_task, args=(task_id, task_type, params)).start()

    return jsonify({'task_id': task_id}), 202


@app.route('/task/<task_id>', methods=['GET'])
def get_task(task_id):
    if task_id not in tasks:
        return 'Task not found', 404
    if tasks[task_id]['status'] == 'running':
        return jsonify({'status': 'running'}), 200

    return jsonify({'status': 'done', 'result': tasks[task_id]['result']}), 200


if __name__ == '__main__':
    app.run(port=5000, debug=True)

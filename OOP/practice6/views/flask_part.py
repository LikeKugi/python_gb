from flask import Flask, render_template, request, jsonify

from Worker import Worker, create_worker

app = Flask(__name__)
app = Flask(__name__, template_folder='templates', static_folder='static')

workers = []


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
@app.route('/index.html', methods=['GET'])
def hello():
    return render_template('index.html')


@app.route('/api/new_worker', methods=['POST'])
def new_worker():
    res = request.json
    print(res)
    nw = create_worker(name=res['value'])
    workers.append(nw)
    print(workers)
    return jsonify({'response': 201}), 201


@app.route('/api/workers', methods=['GET'])
def get_workers():
    sending = [worker.toJSON() for worker in workers]
    return jsonify({'data': sending})


@app.route('/api/workers/<int:worker_id>', methods=['GET', 'PUT', 'DELETE'])
def worker(worker_id):
    if request.method == 'GET':
        print(f'GET: {worker_id}')
        return jsonify({'data': {'r': 'asked worker'}}), 200
    if request.method == 'PUT':
        print(f'MODIFY: {worker_id}')
        return jsonify({'data': {'r': 'modified worker'}}), 200
    if request.method == 'DELETE':
        print(f'DELETE: {worker_id}')
        return jsonify({'data': {'r': 'deleted worker'}}), 200



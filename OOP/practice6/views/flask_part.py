from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

from Worker import Worker, create_worker

app = Flask(__name__, template_folder='templates', static_folder='static')
api = Api(app)

# db = SQLAlchemy(app)

workers_list = []


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
@app.route('/index.html', methods=['GET'])
def hello():
    return render_template('index.html')


@app.route('/workers.html', methods=['GET'])
def workers():
    employees = [1, 2, 3]
    print(workers_list)
    return render_template('workers.html', employees=workers_list)


@app.route('/manage.html', methods=['GET'])
def manage():
    return render_template('manage.html')


@app.route('/api/new_worker', methods=['POST'])
def new_worker():
    res = request.json
    print(res)
    _name = res['name']
    _l_name = res['lastName']
    _passport = res['passport']
    _phone = res['phone']
    _salary = res['salary']
    _cabinet = res['cabinet']
    nw = create_worker(name=_name, last_name=_l_name, salary=_salary, passport_id=_passport, phone_number=_phone,
                       cabinet=_cabinet)
    workers_list.append(nw)
    print(workers_list)
    return jsonify({'response': 201}), 201


@app.route('/api/workers', methods=['GET'])
def get_workers():
    sending = [worker.toJSON() for worker in workers_list]
    return jsonify({'data': sending}), 200


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

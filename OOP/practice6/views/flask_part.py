import os

from flask import Flask, render_template, request, jsonify, make_response
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

from Worker import create_worker

app = Flask(__name__, template_folder='templates', static_folder='static')
api = Api(app)

workers_list = []

# --------------------------------------------------------------------------
#  DB config
# --------------------------------------------------------------------------

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

DB_PATH = 'instance/employees.db'


class Employee(db.Model):
    e_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    passport = db.Column(db.Integer, nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    salary = db.Column(db.Float, nullable=False)
    cabinet = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'{self.e_id}: {self.name} {self.lastname} / {self.passport} {self.phone} {self.salary} {self.cabinet}'


# --------------------------------------------------------------------------
#  API requests
# --------------------------------------------------------------------------

class GetEmployees(Resource):
    """
    all employee
    GET request
    get from db
    """

    def get(self):
        employees = Employee.query.all()
        employee_list = []
        for employee in employees:
            employee_data = {'id': employee.e_id, 'name': employee.name,
                             'lastname': employee.lastname, 'passport': employee.passport, 'phone': employee.phone,
                             'salary': employee.salary, 'cabinet': employee.cabinet}
            employee_list.append(employee_data)
        return {'data': employee_list}, 200


class GetSingleEmployee(Resource):
    """
    one employee
    GET request
    get from db
    """
    def get(self, emp_id):
        employee = Employee.query.get(emp_id)
        if employee is None:
            return {'error': 'not found'}, 404
        else:
            employee_data = {'id': employee.e_id, 'name': employee.name,
                             'lastname': employee.lastname, 'passport': employee.passport, 'phone': employee.phone,
                             'salary': employee.salary, 'cabinet': employee.cabinet}
            return {'data': employee_data}, 200


class AddEmployee(Resource):
    """
    POST request
    add to db
    """

    def post(self):
        if request.is_json:
            res = request.json
            _name = res['name']
            _l_name = res['lastName']
            _passport = res['passport']
            _phone = res['phone']
            _salary = res['salary']
            _cabinet = res['cabinet']
            nw = create_worker(name=_name, last_name=_l_name, salary=_salary, passport_id=_passport,
                               phone_number=_phone,
                               cabinet=_cabinet)
            emp = Employee(name=nw.name, lastname=nw.last_name, passport=nw.passport_id, phone=nw.phone_number,
                           salary=nw.salary, cabinet=nw.cabinet)
            db.session.add(emp)
            db.session.commit()
            return make_response(jsonify({'id': emp.e_id, 'name': emp.name,
                                          'lastname': emp.lastname, 'passport': emp.passport, 'phone': emp.phone,
                                          'salary': emp.salary, 'cabinet': emp.cabinet}))
        else:
            return {'error': 'Must be JSON'}, 400


class UpdateEmployee(Resource):
    """
    PUT request
    edit employee
    """

    def put(self, emp_id):
        if request.is_json:
            emp = Employee.query.get(emp_id)
            if emp is None:
                return {'error': 'not found'}, 404
            else:
                res = request.json
                _name = res['name']
                _l_name = res['lastName']
                _passport = res['passport']
                _phone = res['phone']
                _salary = res['salary']
                _cabinet = res['cabinet']
                nw = create_worker(name=_name, last_name=_l_name, salary=_salary, passport_id=_passport,
                                   phone_number=_phone,
                                   cabinet=_cabinet)
                emp.name = nw.name
                emp.lastname = nw.last_name
                emp.passport = nw.passport_id
                emp.phone = nw.phone_number
                emp.salary = nw.salary
                emp.cabinet = nw.cabinet
                db.session.commit()
                return 'Up to date', 200
        else:
            return {'error': 'Must be JSON'}, 400


class DeleteEmployee(Resource):
    def delete(self, emp_id):
        emp = Employee.query.get(emp_id)
        if emp is None:
            return {'error': 'Not found'}, 404
        db.session.delete(emp)
        db.session.commit()
        return f'{emp_id} was deleted', 200


# --------------------------------------------------------------------------
#  routes
# --------------------------------------------------------------------------

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
@app.route('/index.html', methods=['GET'])
def index():
    if not (os.path.exists(path=DB_PATH)):
        db.create_all()
    return render_template('index.html')

@app.route('/workers.html', methods=['GET'])
def workers():
    employees = Employee.query.all()
    employee_list = []
    for employee in employees:
        employee_data = {'id': employee.e_id, 'name': employee.name,
                         'lastname': employee.lastname, 'passport': employee.passport, 'phone': employee.phone,
                         'salary': employee.salary, 'cabinet': employee.cabinet}
        employee_list.append(employee_data)
    return render_template('workers.html')


@app.route('/manage.html', methods=['GET'])
def manage():
    return render_template('manage.html')

@app.route('/edit.html/<int:emp_id>', methods=['GET'])
def edit(emp_id):
    return render_template('edit.html', emp_id=emp_id)

# --------------------------------------------------------------------------
#  API routes and test routes
# --------------------------------------------------------------------------

api.add_resource(GetEmployees, '/api/workers')
api.add_resource(AddEmployee, '/api/new_worker')
api.add_resource(GetSingleEmployee, '/api/get_worker/<int:emp_id>')
api.add_resource(UpdateEmployee, '/api/update_worker/<int:emp_id>')
api.add_resource(DeleteEmployee, '/api/delete_worker/<int:emp_id>')

@app.route('/api/workers/<int:e_id>', methods=['GET', 'PUT', 'DELETE', 'UPDATE'])
def tester(e_id):
    if request.method == 'GET':
        print(f'GET: {e_id}')
        return jsonify({'data': {'r': 'asked worker'}}), 200
    if request.method == 'PUT':
        print(f'MODIFY: {e_id}')
        return jsonify({'data': {'r': 'modified worker'}}), 200
    if request.method == 'DELETE':
        print(f'DELETE: {e_id}')
        return jsonify({'data': {'r': 'deleted worker'}}), 200
    if request.method == 'UPDATE':
        print(f'UPDATE: {e_id}')
        return jsonify({'data': {'r': 'updated worker'}}), 200

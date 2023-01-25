from flask import Flask, render_template, redirect, url_for, request
from werkzeug.datastructures import ImmutableMultiDict
from service import create_student, create_teacher, update_student
from data import read_file

# ------------------------------------------------------------------------
# app config
# ------------------------------------------------------------------------
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = '1234'

# ------------------------------------------------------------------------
# constants
# ------------------------------------------------------------------------
PATH_TEACHERS = 'storage/teachers.bin'
PATH_STUDENTS = 'storage/students.bin'
PATH_KLASSES = 'storage/klasses.bin'


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/students', methods=['GET', 'POST'])
@app.route('/students.html', methods=['GET', 'POST'])
def students():
    klasses = read_file(path='storage/klasses.bin')

    if request.method == "POST":
        res_id = request.form['id']
        res_grades = {}

        for key, value in request.form.items():
            if key not in ('id', 'name') and value:
                res_grades.update({key: int(value)})

        result = {
            'id': res_id,
            'grades': res_grades
        }
        res_name = request.form.get('name', None)
        if res_name:
            result.update({'name': res_name})
        update_student(result)

    return render_template('students.html', klass=klasses)


@app.route('/klasses', methods=['GET', 'POST'])
@app.route('/klasses.html', methods=['GET', 'POST'])
def klasses():
    klasses = read_file(path='storage/klasses.bin')
    print(klasses)
    return render_template('klasses.html', klass=klasses)

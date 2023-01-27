from flask import Flask, render_template, request
from service import create_student, create_teacher, update_student, add_student_to_klass, del_student, \
    add_teacher_to_klass
from data import read_file, create_json

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


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
@app.route('/index.html', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/students', methods=['GET', 'POST'])
@app.route('/students.html', methods=['GET', 'POST'])
def students():
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
    klasses = read_file(path='storage/klasses.bin')
    return render_template('students.html', klass=klasses)


@app.route('/klasses', methods=['GET', 'POST'])
@app.route('/klasses.html', methods=['GET', 'POST'])
def klasses():
    klasses = read_file(path='storage/klasses.bin')
    return render_template('klasses.html', klass=klasses)


@app.route('/teachers', methods=['GET', 'POST'])
@app.route('/teachers.html', methods=['GET', 'POST'])
def teachers():
    klasses = read_file(path='storage/klasses.bin')
    return render_template('teachers.html', klass=klasses)


@app.route('/performance', methods=['GET', 'POST'])
@app.route('/performance.html', methods=['GET', 'POST'])
def performance():
    klasses = read_file(path='storage/klasses.bin')
    students = sorted(klasses.students.values(), key=lambda x: sum([el or 0 for el in x.grades.values()] ) / len(x.grades.values()) ,reverse=True)
    return render_template('performance.html', students=students)


@app.route('/opportunities', methods=['GET', 'POST'])
@app.route('/opportunities.html', methods=['GET', 'POST'])
def opportunities():
    klasses = read_file(path='storage/klasses.bin')
    if request.method == "POST":
        req_option = request.form['options']
        match req_option:
            case 'add':
                student = create_student()
                add_student_to_klass(student)
            case 'teacher':
                req_lesson = request.form['new_lesson']
                teacher = create_teacher(lesson=req_lesson)
                add_teacher_to_klass(teacher)
            case 'export':
                create_json(klasses.students)
            case 'del':
                req_del = request.form['student']
                del_student(int(req_del))
            case _:
                print('smth wrong')
    klasses = read_file(path='storage/klasses.bin')
    return render_template('opportunities.html', klass=klasses)

from flask import Flask, render_template, redirect, url_for, request
from service import create_student, create_teacher


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = '1234'

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/students', methods=['GET', 'POST'])
@app.route('/students.html', methods=['GET', 'POST'])
def students():
    create_teacher()
    return render_template('students.html')


@app.route('/klasses', methods=['GET', 'POST'])
@app.route('/klasses.html', methods=['GET', 'POST'])
def klasses():
    create_student()
    return render_template('klasses.html')
from flask import Flask, render_template, redirect, url_for

from .get_questions import get_dict_questions
from .check_question_form import ChooseQuestionForm as CQF

from .answer_storage import Answer
from .save_answer_storage import save_answer

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = '1234'

current_answer = Answer()

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    dict_questions = get_dict_questions()
    form = CQF()
    if form.questions.data and form.answer.data:
        index = int(form.questions.data)
        save_answer(dict_questions, index, form.answer.data)
        return redirect(url_for('question'))
    form.questions.choices = [(key, value.get('question_text')) for key, value in dict_questions.items()]
    return render_template('index.html', form=form)


@app.route('/question', methods=['GET', 'POST'])
def question():
    return render_template('question.html')

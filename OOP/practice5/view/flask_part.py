from flask import Flask, render_template, request

from controller import confirm_expression, eval_expression, init_calc, add_calc

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = '1234'

history = init_calc()


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
def index():
    answer_text = ''
    answer_val = 0
    res = {}
    if request.method == 'POST':
        print(request.form)
        if (q := request.form.get('exp')):
            print(confirm_expression(q))
            res = add_calc(history=history, value=q)
            print(res)
            answer_text, answer_val = eval_expression(q)
    return render_template('index.html', answer=answer_text, answer_val=answer_val, history=res)
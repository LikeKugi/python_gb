from flask import Flask, render_template
from base import get_laptops, save_laptops


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = '1234'


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    laptops = get_laptops()
    return render_template('index.html', laptops=laptops)

import os

from flask import Flask, render_template, redirect, url_for, request
from base import get_laptops, write_json, filter_laptops
from .add_form import UploadForm as UF
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = '1234'
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png']
app.config['UPLOAD_PATH'] = 'flask_part/static/img'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    laptops = get_laptops()
    return render_template('index.html', laptops=laptops)


@app.route('/add', methods=['GET', 'POST'])
@app.route('/add.html', methods=['GET', 'POST'])
def upload_page():
    form = UF()
    if form.product_name.data:
        print()
        uploaded_file = request.files['image']
        if uploaded_file:
            filename = secure_filename(uploaded_file.filename)
            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
            print(filename)
        else:
            filename = 'empty.jpg'

        print(f'name = {form.product_name.data}')
        print(f'cpu = {form.cpu.data}')
        print(f'ram = {form.ram.data}')
        print(f'storage = {form.storage.data}')
        print(f'inches = {form.screen_inches.data}')
        print(f'screen = {form.screen_property.data}')
        print(f'price = {form.price.data}')
        print(f'image = {form.image}')

        new_laptop = {
            'productName': form.product_name.data,
            'image': filename,
            'cpu': form.cpu.data,
            'ram': f'{form.ram.data}GB',
            'storage': f'{form.storage.data}GB',
            'screen': f'{form.screen_inches.data}, {form.screen_property.data}',
            'price': f'{form.price.data}'
        }
        print(new_laptop)
        write_json(new_laptop)

        return redirect(url_for('index'))

    return render_template('add.html', form=form)

@app.route('/cpu')
@app.route('/cpu.html')
def filter_cpu():
    laptops = filter_laptops('cpu')
    return render_template('index.html', laptops=laptops)

@app.route('/ram')
@app.route('/ram.html')
def filter_ram():
    laptops = filter_laptops('ram')
    return render_template('index.html', laptops=laptops)

@app.route('/storage')
@app.route('/storage.html')
def filter_storage():
    laptops = filter_laptops('storage')
    return render_template('index.html', laptops=laptops)

@app.route('/inches')
@app.route('/inches.html')
def filter_inches():
    laptops = filter_laptops('screen')
    return render_template('index.html', laptops=laptops)
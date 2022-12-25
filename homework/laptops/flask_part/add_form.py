from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired


class UploadForm(FlaskForm):
    product_name = StringField(u'Laptop Name', [DataRequired()])
    cpu = StringField(u'CPU model', [DataRequired()])
    ram = IntegerField(u'RAM', [DataRequired()])
    storage = IntegerField(u'Storage', [DataRequired()])
    screen_inches = FloatField(u'Inches', [DataRequired()])
    screen_property = StringField(u'Screen property', [DataRequired()])
    price = IntegerField(u'$ Price', [DataRequired()])
    image = FileField(u'Image File', validators=[FileAllowed(['jpg', 'png'], '.jpg or .png files only!')])
    submit = SubmitField('Upload')

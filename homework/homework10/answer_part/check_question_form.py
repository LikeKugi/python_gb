from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class ChooseQuestionForm(FlaskForm):
    questions = SelectField('Выберите вопрос', validators=[DataRequired()])
    answer = TextAreaField('Ответ на вопрос',
                           render_kw={"rows": 10,
                                      "cols": 50},
                           validators=[DataRequired()])
    submit = SubmitField('Ответить')

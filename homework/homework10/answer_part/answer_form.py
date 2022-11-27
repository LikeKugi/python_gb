from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField



class AnswerQuestionForm(FlaskForm):
    answer = TextAreaField('Ответ на вопрос',
                           render_kw={"rows": 70,
                                      "cols": 12})
    submit_answer = SubmitField

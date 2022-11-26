from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def set_menu_buttons() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    ask_question_button = KeyboardButton('Задать вопрос')
    questions_button = KeyboardButton('Мои вопросы')
    answers_button = KeyboardButton('Ответы на мои вопросы')
    keyboard.add(ask_question_button, questions_button, answers_button)
    return keyboard

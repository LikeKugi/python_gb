import telebot

from bot_logic import set_menu_buttons as menu
from bot_logic import set_continue_keyboards as c_yes_no
from bot_logic import set_quiz_keyboards as q_yes_no
from bot_logic import get_url_cat as cat_url
from bot_logic import BotState as BS
from bot_logic import txt_logger, user_logger
from bot_logic import main_register
from bot_logic import get_users_ids
from calcing import Calculator
from quiz import QuizNumber

# ----------------------------------------------------------------------
# variables and constants
# ----------------------------------------------------------------------
token = ''

bot = telebot.TeleBot(token)

# FSM
# do_calc -> calc: bool
# do_quiz -> quiz: bool
# stop_state -> calc = False; quiz = False
state = BS()

# the number for quiz
quiz_number = QuizNumber()

# default answers
CALCING = 'Введите выражение, которое надо посчитать'
QUIZ_GAME = 'Я загадал число от 0 до 1000 включительно, отгадай'
UNKNOWN = 'Неизвестная команда'


# ----------------------------------------------------------------------
# OTHER FUNCTIONS
# ----------------------------------------------------------------------
def send_cat(message):
    """
    sends a picture of cat
    """
    bot.send_photo(message.chat.id, cat_url())


def calc_expression(message):
    """
    turn on calculator state
    """
    bot.send_message(message.chat.id, CALCING)
    if not state.calc:
        state.do_calc()


def go_calc(message):
    try:
        expression = Calculator(message.text)
    except Calculator.CalculatorException as CE:
        bot.send_message(message.chat.id, str(CE), reply_markup=c_yes_no())
    else:
        bot.send_message(message.chat.id, str(expression), reply_markup=c_yes_no())


def quiz_game(message):
    """
    turn on quiz game
    """
    bot.send_message(message.chat.id, QUIZ_GAME)
    QuizNumber()
    if not state.quiz:
        state.do_quiz()


def go_quiz(message):
    try:
        msg = quiz_number.check(int(message.text))
    except ValueError as e:
        bot.send_message(message.chat.id, str(e), reply_markup=q_yes_no())
    except Exception as e:
        bot.send_message(message.chat.id, str(e), reply_markup=q_yes_no())
    else:
        bot.send_message(message.chat.id, msg, reply_markup=q_yes_no())


# ----------------------------------------------------------------------
# CALLS
# ----------------------------------------------------------------------


commands = {
    'Хочу котика!': send_cat,
    'Посчитать': calc_expression,
    'Угадаю число от 0 до 1000': quiz_game
}


# ----------------------------------------------------------------------
# BOT COMMANDS
# ----------------------------------------------------------------------
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет!', reply_markup=menu())


@bot.message_handler(commands=['register'])
@user_logger
def register_user(message):
    txt = main_register(message)
    bot.send_message(message.chat.id, txt)


@bot.message_handler(commands=['dospam'])
def spam_users(message):
    users = get_users_ids()
    for user in users:
        bot.send_message(user, text="YOU'RE OWNED")


@bot.message_handler(func=lambda message: True)
@txt_logger
def message_write(message):
    query = message.text
    if state.calc:
        go_calc(message)
    elif state.quiz:
        go_quiz(message)
    elif q := commands.get(query, False):
        q(message)
    else:
        bot.send_message(message.chat.id, UNKNOWN)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'Y_calc':
        calc_expression(call.message)
    if call.data == 'Y_quiz':
        quiz_game(call.message)
    elif call.data == 'all_stop':
        state.stop_state()


# ----------------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------------
if __name__ == '__main__':
    bot.polling(none_stop=True)

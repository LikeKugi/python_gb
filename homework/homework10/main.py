# Telegram bot client
import telebot

from bot_logic import set_menu_buttons as menu
from bot_logic import BotState

from question_xml import add_question_node as xml_ask
from question_xml import looking_for_questions as xml_get_questions

# ----------------------------------------------------------------------
# variables and constants
# ----------------------------------------------------------------------
token: str = ''
bot = telebot.TeleBot(token)

#FSM of bot
state = BotState()

# @formatter:off
ASK_QUESTION        :str = 'Задайте свой вопрос'
ASKED_QUESTIONS     :str = 'Вопросы, которые Вы задавали'
ANSWERED_QUESTIONS  :str = 'Вопросы, на которые есть ответы'
# @formatter:on


# ----------------------------------------------------------------------
# BOT STATES FUNCTIONS
# ----------------------------------------------------------------------
def turn_ask_state(message) -> None:
    """
    FSM -> turn off all states and turn on a state for question from user
    :param message: message of telegram
    :return: None
    """
    bot.send_message(message.chat.id, ASK_QUESTION)
    if not state.ask:
        state.do_ask()


def go_ask(message) -> None:
    """
    write the question to xml file
    :param message: message
    :return: None
    """
    xml_ask(message)
    state.stop_state()


def turn_asked_state(message) -> None:
    """
    send all the questions that user asked to the user
    :param message: message
    :return: None
    """
    bot.send_message(message.chat.id, ASKED_QUESTIONS)
    questions = xml_get_questions(message.from_user.id)
    go_asked(questions, message.chat.id)


def go_asked(asked_questions: dict, chat_id: int, *, asked_flag=False) -> None:
    """
    the function itself that sends questions to the user
    :param asked_questions: dict
        questions
    :param chat_id: int
        chat ID of the user
    :param asked_flag: bool
        False if unanswered and answered questions
        True if only answered questions
    :return: None
    """
    if not asked_questions:
        bot.send_message(chat_id, 'Нет элементов')
        return
    for time, question in asked_questions.items():
        ask, answer = question[0], question[1]
        if answer:
            bot.send_message(chat_id, f'{time}:\n{ask}\nanswer:\n{answer}')
        else:
            if not asked_flag:
                bot.send_message(chat_id, f'{time}:\n{ask}')
    state.stop_state()


def turn_answered_state(message) -> None:
    """
    send all answered questions for the user
    :param message: message
    :return: None
    """
    bot.send_message(message.chat.id, ANSWERED_QUESTIONS)
    questions = xml_get_questions(message.from_user.id, need_answer=True)
    go_asked(questions, message.chat.id, asked_flag=True)


# ----------------------------------------------------------------------
# BOT FUNCTIONS CALLS
# ----------------------------------------------------------------------
# @formatter:off
state_commands = {
    'Задать вопрос'         :   turn_ask_state,
    'Мои вопросы'           :   turn_asked_state,
    'Ответы на мои вопросы' :   turn_answered_state
}
# @formatter:on


# ----------------------------------------------------------------------
# BOT COMMANDS
# ----------------------------------------------------------------------
@bot.message_handler(commands=['start'])
def start_message(message) -> None:
    bot.send_message(message.chat.id, 'Привет!', reply_markup=menu())


@bot.message_handler(func=lambda message: True)
def message_getter(message) -> None:
    query = message.text
    if state.ask:
        go_ask(message)
    elif q := state_commands.get(query, False):
        q(message)


# ----------------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------------
if __name__ == '__main__':
    bot.polling(none_stop=True)

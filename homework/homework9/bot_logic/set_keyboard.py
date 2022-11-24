from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton


def set_menu_buttons() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    kitty_button = KeyboardButton('Хочу котика!')
    calc_button = KeyboardButton('Посчитать')
    game_button = KeyboardButton('Угадаю число от 0 до 1000')
    keyboard.add(kitty_button, calc_button, game_button)
    return keyboard


def set_continue_keyboards() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    yes_choose = InlineKeyboardButton(text='ПРОДОЛЖИТЬ', callback_data='Y_calc')
    no_choose = InlineKeyboardButton(text='СТОП', callback_data='all_stop')
    keyboard.add(yes_choose, no_choose)
    return keyboard


def set_quiz_keyboards() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    yes_choose = InlineKeyboardButton(text='ПРОДОЛЖИТЬ', callback_data='Y_quiz')
    no_choose = InlineKeyboardButton(text='ХВАТИТ', callback_data='all_stop')
    keyboard.add(yes_choose, no_choose)
    return keyboard

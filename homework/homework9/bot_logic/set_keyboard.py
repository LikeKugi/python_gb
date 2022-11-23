from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton


def set_menu_buttons():
    keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    kitty_button = KeyboardButton('Хочу котика!')
    calc_button = KeyboardButton('Посчитать')
    game_button = KeyboardButton('Угадаю число от 0 до 1000')
    keyboard.add(kitty_button, calc_button, game_button)
    return keyboard


def set_continue_keyboards():
    keyboard = InlineKeyboardMarkup()
    yes_choose = InlineKeyboardButton(text='ДА', callback_data='stay')
    no_choose = InlineKeyboardButton(text='НЕТ', callback_data='stop_calc')
    keyboard.add(yes_choose, no_choose)
    return keyboard

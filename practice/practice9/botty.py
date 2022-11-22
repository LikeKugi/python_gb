import telebot
import time
import requests

token = ''

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello world!')


@bot.message_handler(commands=['cat'])
def send_cat(message):
    url = f'https://cataas.com/cat?t=${time.time()}'
    bot.send_photo(message.chat.id, url)


@bot.message_handler(commands=['weather'])
def send_weather(message):
    api_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': 'Saint Petersburg',
        'appid': '11c0d3dc6093f7442898ee49d2430d20',
        'units': 'metric'
    }
    res = requests.get(api_url, params=params)
    data = res.json()
    print(data)
    answer = f"""{data['name']}
    t {data['main']['temp']}
    p {data['main']['pressure']}
    clouds {data['clouds']}
    """
    bot.send_message(message.chat.id, answer)


@bot.message_handler(func=lambda message: True)
def message_write(message):

    equals = message.text
    if equals.replace('/','').replace('*','').replace('-','').replace('+','').replace('.','').isdigit():
        answer = f'{message.text} = {eval(message.text)}'
        bot.send_message(message.chat.id, answer)
    with open('text.txt', 'a', encoding='utf-8') as ouf:
        print(message.text, file=ouf)


bot.infinity_polling()

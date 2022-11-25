import time


def txt_logger(func):
    def inner(*args, **kwargs):
        msg = args[0]
        with open('logs_txt.txt', 'a', encoding='utf-8') as ouf:
            print(f'{time.strftime("%H:%M:%S")}: {msg.from_user.id} user id:\n\t{msg.text}', file=ouf)
        return func(*args, **kwargs)
    return inner


def user_logger(func):
    def inner(*args, **kwargs):
        msg = args[0]
        with open('user_logs.txt','a', encoding='utf-8') as ouf:
            print(f'Try register:\n\t{time.strftime("%H:%M:%S")} {msg.from_user.id}', file=ouf)
        return func(*args, **kwargs)
    return inner

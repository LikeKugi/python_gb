import time

from view import app

def print_hi():
    print('Running: ' + time.strftime("%d.%m.%Y %H:%M:%S"))
    print('hi')


if __name__ == '__main__':
    print_hi()
    app.run(host="localhost", port=5000, debug=True)
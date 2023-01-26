import time
import os

from view_part import app
from service import create_random_klass

PATH = 'storage/klasses.bin'

def print_hi():
    print('Running: ' + time.strftime("%d.%m.%Y %H:%M:%S"))
    print('hi')
    print('EXISTS: ',os.path.exists(PATH))
    if not (os.path.exists(PATH) and os.path.getsize(PATH) > 0):
        create_random_klass()


if __name__ == '__main__':
    print_hi()
    app.run(host="localhost", port=5000, debug=True)

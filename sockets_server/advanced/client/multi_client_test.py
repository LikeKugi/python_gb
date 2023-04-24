import threading
from _thread import *
import socket

BUFF_SIZE = 1024  # buffer size
PORT = 9595
HOST = (socket.gethostname(), PORT)

FILENAME = '20220513_133035.jpg'

locked = threading.Lock()


def clients(file_name):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(HOST)

    with open(file_name, 'rb') as inf:
        client.sendfile(inf)

    locked.release()


def main():
    for i in range(11):
        locked.acquire()
        file_name = f'{i}.jpg'
        start_new_thread(clients, (file_name,))


if __name__ == '__main__':
    main()

import socket
import hashlib
import time

from _thread import *
import threading

BUFF_SIZE = 1024
PORT = 9595

HOST = (socket.gethostname(), PORT)

receive_lock = threading.Lock()


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4 + TCP
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # immediately reuse socket address after close server
    try:
        s.bind(HOST)
        s.listen()
        print('server is running')

        while True:
            client, addr = s.accept()
            receive_lock.acquire()
            print(f'New connection from {addr}')

            start_new_thread(receive_jpg, (client, addr))

    except KeyboardInterrupt:
        print('Close connection')
    except Exception as e:
        print(e)
    finally:
        s.close()


def receive_jpg(client: socket.socket, addr):
    print(time.time())
    print(client)
    try:
        data = client.recv(BUFF_SIZE)
        name = hashlib.md5(str(addr).encode('UTF-8') + str(time.time()).encode('UTF-8'))
        while data:
            try:
                with open(f'{name.hexdigest()}.jpg', 'ab') as ouf:
                    ouf.write(data)
            except PermissionError:
                continue
            data = client.recv(BUFF_SIZE)
    except Exception as e:
        print(e)
    finally:
        print('All data has been received')
        print(f'Connection from {addr} closed')
        print()
        client.close()
        receive_lock.release()


if __name__ == '__main__':
    main()

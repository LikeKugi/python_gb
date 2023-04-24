import socket
import hashlib
import time

BUFF_SIZE = 1024
PORT = 9595

HOST = (socket.gethostname(), PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4 + TCP
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # immediately reuse socket address after close server
s.bind(HOST)
s.listen()

print('server is running')

while True:
    client, addr = s.accept()
    print(f'New connection from {addr}')

    data = client.recv(BUFF_SIZE)
    name = hashlib.md5(str(addr).encode('UTF-8') + str(time.time()).encode('UTF-8'))
    while data:
        with open(f'{name.hexdigest()}.jpg', 'ab') as ouf:
            ouf.write(data)
        data = client.recv(BUFF_SIZE)

    print('All data has been received')
    print(f'Connection from {addr} closed')
    client.close()

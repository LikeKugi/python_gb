import socket

BUFF_SIZE = 1024  # buffer size
PORT = 9595

HOST = (socket.gethostname(), PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(HOST)

FILENAME = '20220513_133035.jpg'
with open(FILENAME, 'rb') as inf:
    client.sendfile(inf)

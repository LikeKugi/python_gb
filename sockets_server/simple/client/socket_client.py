import socket

from client_functions import send_data, send_any_data

BUFF_SIZE = 8 # buffer size

HOST = socket.gethostname(), 9595

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(HOST)

msg = ''



# while True:
#     data = client.recv(BUFF_SIZE)
#     if not len(data):
#         break
#     msg += data.decode('UTF-8')

# send_data(client)
send_any_data(client, {1: 'one', 2: 'two', 3: 'three'})

print(msg)
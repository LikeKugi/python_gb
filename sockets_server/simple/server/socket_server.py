import socket

from server_functions import get_request, get_request_anydata

BUFF_SIZE = 8

HOST = (socket.gethostname(), 9595)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4 + TCP
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # immediately reuse socket address after close server
s.bind(HOST)
s.listen()

print('server is running')

# while True:
#     conn, addr = s.accept() # conn (connection) - client addr (address) - address of client
#     res = b'connected'
#     conn.send(res)
#
#     conn.close()

conn, addr = s.accept()
print(f'connected from {addr}')
# req = get_request(conn, BUFF_SIZE)
req = get_request_anydata(conn, BUFF_SIZE)
print(req)

conn.close()


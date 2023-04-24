import socket
import select

HEADER_LENGTH = 10
HOST = ('', 10000)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(HOST)
server.listen()

print('Server is on. Listening to connections')

sockets_list = [server]
clients_list = {}


def receive_msg(client: socket.socket):
    try:
        msg_header = client.recv(HEADER_LENGTH)
        if not len(msg_header):
            return False

        msg_length = int(msg_header.decode('UTF-8').strip())

        return {
            'header': msg_header,
            'data': client.recv(msg_length).decode('UTF-8')
        }
    except Exception:
        return False


while True:
    rs, _, es = select.select(sockets_list, [], sockets_list)  # read_list, write_list, error_list

    for _socket in rs:
        if _socket == server:
            client, addr = server.accept()

            user = receive_msg(client)
            if user is False:
                continue

            sockets_list.append(client)
            clients_list[client] = user

        else:
            msg = receive_msg(client)
            if msg is False:
                print(f'connection from {addr} has been interrupted')
                sockets_list.remove(_socket)
                del clients_list[_socket]
                continue

        user = clients_list[_socket]

        for client in clients_list:
            if client is not _socket:
                client.send(f'New message from {user["data"]} is {msg["data"]}')

    for _socket in es:
        sockets_list.remove(_socket)
        del clients_list[_socket]

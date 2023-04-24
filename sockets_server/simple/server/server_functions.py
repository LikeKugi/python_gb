import pickle
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import socket


def get_request(conn, BUFF_SIZE):
    """
    get data from connection
    :param conn: connection of socket
    :param BUFF_SIZE: size of buffer
    :return: decoded data
    """
    print('waiting for request')
    req = ''
    while True:
        data = conn.recv(BUFF_SIZE)
        if not len(data):
            return req
        req += data.decode()


def get_request_anydata(conn: 'socket', BUFF_SIZE):
    """
    get data from client serialized by pickle
    :param conn: connection of socket
    :param BUFF_SIZE: size of buffer
    :return: decoded data
    """
    print('waiting for any data')
    req = b''

    while True:
        data = conn.recv(BUFF_SIZE)
        if not len(data):
            break
        print(data)
        req += data
    print(req)
    return pickle.loads(req)


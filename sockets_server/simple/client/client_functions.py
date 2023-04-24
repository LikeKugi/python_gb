import pickle


def send_data(client, data=b'GET / HTTP/1.1\r\nHost:localhost:9595\r\n\r\n'):
    sent = 0
    print('sending', data)
    req = data

    # while sent < len(req):
    #     sent = sent + client.send(req[sent:])

    client.sendall(data)


def send_any_data(client, data=b'GET / HTTP/1.1\r\nHost:localhost:9595\r\n\r\n'):
    sending_data = pickle.dumps(data)
    client.sendall(sending_data)
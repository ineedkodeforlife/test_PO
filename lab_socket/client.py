import socket
import re


status = False
HOST = '127.0.0.1'
PORT = 50007


def verify_server(to_email, text_message):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    match = re.match(pattern, to_email)
    return match is not None


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # s.sendall(b'Hello, world')
    # data = s.recv(1024)
    # print('Received', repr(data))
    while not status:
        em_adress, msg = input('Введите адрес электронной почты, на который хотите отправить сообщение\n'), \
            input('Введите сообщение, которое вы хотите отправить\n')
        status = verify_server(em_adress, msg)

    data_to_send = em_adress + "~" + msg
    s.sendall(data_to_send.encode('utf-8'))
    data = s.recv(1024)
    print('Received', repr(data))

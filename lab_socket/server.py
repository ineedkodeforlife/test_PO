import socket
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import randint

HOST = '127.0.0.1'
PORT = 50007


def generate_id() -> int:
    return int(randint(10000, 99999))


def take_key(value: str):
    with open('log_pass.env', 'r') as file:
        for string in file:
            key_value = string.split('=')
            if key_value[0].replace(" ", '') == value:
                if key_value[1].isdigit():
                    return int(key_value[1])
                return key_value[1].rstrip()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                print('gg')
                break

            data_dec = data.decode('utf-8')
            to_email, text_message = data_dec.split('~')
            id_msg = generate_id()
            email = take_key('EMAIL_LOGIN')
            message = MIMEMultipart()
            message['From'] = email
            message['To'] = ', '.join([email, to_email])
            message['Subject'] = f'[Ticket #{id_msg}] Mailer'
            message.attach(MIMEText(text_message, 'plain'))

            try:
                with SMTP(take_key('SMTP_HOST'), take_key('SMTP_PORT')) as server:
                    server.starttls()
                    server.login(email, take_key('EMAIL_PASSWORD'))
                    server.send_message(message)
            except Exception as e:
                print(e)

            conn.sendall(data)

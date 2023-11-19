from imaplib import IMAP4_SSL
from time import sleep
from email.header import decode_header
import email
import re
import os


def take_key(value: str):
    with open('log_pass.env', 'r') as file:
        for string in file:
            key_value = string.split('=')
            if key_value[0].replace(" ", '') == value:
                if key_value[1].isdigit():
                    return int(key_value[1])
                return key_value[1].rstrip()


def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True).decode('utf-8')


def verify_write_file(name_file, text_msg, id_msg=''):
    if os.path.isfile(name_file):
        with open(name_file, 'a', encoding='utf-8') as file:
            file.write(f'{id_msg} {text_msg}')
    else:
        with open(name_file, 'w', encoding='utf-8') as file:
            file.write(f'{id_msg} {text_msg}')


def pars_email_msg():
    with IMAP4_SSL(take_key('IMAP_HOST'), take_key('IMAP_PORT')) as M:
        rc, resp = M.login(take_key('EMAIL_LOGIN'), take_key('EMAIL_PASSWORD'))
        M.select()
        typ, data = M.search(None, 'ALL')
        for num in list(reversed(data[0].split()))[:10]:
            typ, data = M.fetch(num, "(BODY[HEADER.FIELDS (SUBJECT)])")
            typ_1, data_1 = M.fetch(num, '(RFC822)')
            headers = data[0][1].decode('utf-8')
            msg_body = data_1[0][1]
            msg = email.message_from_bytes(msg_body)
            text_msg = get_body(msg)
            decoded_headers = decode_header(headers)

            # Извлечение темы сообщения
            subject = None
            for decoded_header in decoded_headers:
                if decoded_header[1]:
                    subject = decoded_header[0].decode(decoded_header[1])
                else:
                    subject = decoded_header[0]
            pattern = r'\[Ticket #(\d+)\] Mailer'
            match = re.search(pattern, subject)
            id_msg = re.findall("\d+", subject)
            if match:
                verify_write_file('success_request.log', text_msg, id_msg[0])
            else:
                verify_write_file('error_request.log', text_msg)


    sleep(take_key('PERIOD_CHECK'))


if __name__ == '__main__':
    pars_email_msg()

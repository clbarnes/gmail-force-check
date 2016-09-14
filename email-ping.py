#!/usr/bin/python
import smtplib
import time
from email.mime.text import MIMEText
import json
import base64 as b64


def get_settings():
    with open('settings.json') as f:
        return json.load(f)


def make_from_address(from_username, from_suffix):
    user, server = from_username.split('@')
    return '{}+{}@{}'.format(user, from_suffix, server)


settings = get_settings()

to_list = settings['to_list']  # add recipient (your remote account) here
from_email = make_from_address(settings['from_username'], settings['from_suffix'])  # email from which the e-mail is sent; must be accepted by SMTP

s = smtplib.SMTP_SSL(settings['smtp_address'])  # SMTP address
s.login(settings['from_username'], b64.b64decode(settings['enc_password']).decode())  # ('smtp login', 'smtp password')

for to in to_list:
    msg = MIMEText('server status: OK')
    msg['Subject'] = '{} {}'.format(settings['subject'], time.ctime())
    msg['From'] = from_email
    msg['To'] = to
    print(msg.as_string())
    s.sendmail(from_email, [to], msg.as_string())


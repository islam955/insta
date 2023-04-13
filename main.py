import requests
from time import sleep
import string
import random
with open("user_agents.txt") as f:
    user_agents = f.readlines()
user_agents = [ua.strip() for ua in user_agents]
random_letters = ''.join(random.choices(string.ascii_letters, k=3))
random_rest = ''.join(random.choices(string.ascii_letters + string.digits, k=18))
device_id = f'ZDk{random_letters}ALAA{random_rest}'
length_x_csrftoken = 32
characters = string.ascii_letters + string.digits
random_string = ''.join(random.choice(characters) for i in range(length_x_csrftoken))
x_csrftoken = random_string
first_names = ['Emma', 'Olivia', 'Ava', 'Isabella', 'Sophia', 'Mia', 'Charlotte', 'Amelia', 'Evelyn', 'Abigail', 'Emily', 'Harper', 'Elizabeth', 'Avery', 'Sofia', 'Ella', 'Madison', 'Scarlett', 'Victoria', 'Aria', 'Grace', 'Chloe', 'Camila', 'Penelope', 'Riley', 'Layla', 'Lillian', 'Nora', 'Zoey', 'Mila', 'Hannah', 'Aurora', 'Leah', 'Savannah', 'Audrey', 'Brooklyn', 'Bella', 'Claire', 'Stella', 'Maya', 'Lucy', 'Ellie', 'Nova', 'Genesis', 'Naomi', 'Madelyn', 'Elena']
last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Perez', 'Taylor', 'Anderson', 'Wilson', 'Jackson', 'Moore', 'Martin', 'Lee', 'Lewis', 'Walker', 'Hall', 'Allen', 'Young', 'King', 'Wright', 'Scott', 'Green', 'Baker', 'Adams', 'Nelson', 'Carter', 'Mitchell', 'Perez', 'Roberts', 'Turner', 'Phillips', 'Campbell', 'Parker', 'Evans', 'Edwards', 'Collins', 'Stewart', 'Sanchez', 'Morris', 'Rogers', 'Reed']
first_name = random.choice(first_names)
last_name = random.choice(last_names)
full_name = f'{first_name} {last_name}'
length_pass = 12
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for ii in range(length_pass))
#get mail
mail = requests.session()
email = mail.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox').json()[0]
username = email.split('@')[0]
domain = email.split('@')[1]
print('Mail Inbox created ==> ' + email)
#send code
emailConfirmation = requests.session()
url = 'https://www.instagram.com/api/v1/accounts/send_verify_email/'
headers = {
    'authority': 'www.instagram.com',
    'method': 'POST',
    'path': '/api/v1/accounts/send_verify_email/',
    'scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/signup/email/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': f'{user_agents}',
    'x-asbd-id': '198387',
    'x-csrftoken': f'{x_csrftoken}',
    'x-ig-app-id': '1217981644879628',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '1007275653',
    'x-requested-with': 'XMLHttpRequest'
}
data = {
     "device_id": f"{device_id}",
     "email": f"{email}"
}
ver = emailConfirmation.post(url, headers=headers, data=data)
print(ver.json())
x_csrftoken = headers['x-csrftoken']
#wait for the code
while True:
    sent_mail = mail.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={username}&domain={domain}').json()
    print('Checking The Code...')
    sleep(5)
    if sent_mail:
        break
idd = sent_mail[0]['id']
sent_code = mail.get(f'https://www.1secmail.com/api/v1/?action=readMessage&login={username}&domain={domain}&id={idd}').json()
code = sent_code['subject'][:6]
print('Confirmation Code is ' + code)
#check_confirmation_code
url = 'https://www.instagram.com/api/v1/accounts/check_confirmation_code/'
headers = {
    'authority': 'www.instagram.com',
    'method': 'POST',
    'path': 'api/v1/accounts/check_confirmation_code/',
    'scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/signup/email/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': f'{user_agents}',
    'x-asbd-id': '198387',
    'x-csrftoken': f'{x_csrftoken}',
    'x-ig-app-id': '1217981644879628',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '1007275653',
    'x-requested-with': 'XMLHttpRequest'
}
data = {
     "code": f"{code}",
     "device_id": f"{device_id}",
     "email": f"{email}"
}
check_confirmation_code = requests.post(url, headers=headers, data=data)
if check_confirmation_code.json()['status'] == 'ok':
    print('Check Confirmation Code Done')
signup_code = check_confirmation_code.json()['signup_code']
#web_create_ajax
url = 'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/'
headers = {
    'authority': 'www.instagram.com',
    'method': 'POST',
    'path': '/api/v1/web/accounts/web_create_ajax/',
    'scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/signup/username/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': f'{user_agents}',
    'x-asbd-id': '198387',
    'x-csrftoken': f'{x_csrftoken}',
    'x-ig-app-id': '1217981644879628',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '1007275653',
    'x-requested-with': 'XMLHttpRequest'
}
data = {
    "enc_password": "#PWD_INSTAGRAM_BROWSER:10:1681043790:AT9QANinnDHOrtx6YlYwmlLfv/Uw1zPxvvOJ6gruL/XlW09SpWIfUvoKAy+EylM36t1hWl5cjC3LFP1H8RSlNNvJ3rxV5IjugsudPDITkWVEPnengkFsnTZlD1QmJ4YtSgFegvSKJWpuG+02m600Zaobv90X3XE=",
    "email": f"{email}",
    "username": f"{username}",
    "first_name": f"{full_name}",
    "month": "4",
    "day": "9",
    "year": "1987",
    "client_id": f"{device_id}",
    "seamless_login_enabled": "1",
    "tos_version": "row",
    "force_sign_up_code": f"{signup_code}"
}
web_create_ajax = requests.post(url, headers=headers, data=data)
print(web_create_ajax.text)
print(full_name)
print(username)
print('done')
sleep(5*60)

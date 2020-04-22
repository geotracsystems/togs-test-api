import json
import time
import requests
from utils.api_defs import oauth

expire_time = 0
access_token = 'invalidtoken'


def oauth2_token(env):
    global expire_time
    global access_token

    if expire_time < time.time():
        data = (
            f"grant_type=password&"
            f"client_id={env['client_id']}&"
            f"client_secret={env['client_secret']}&"
            f"username={env['username']}&"
            f"password={env['password']}&"
            f"scope={env['scope']}"
        )
        header = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"}

        response = requests.post(env['url'], headers=header, data=data)
        print(response.content)
        access_token = json.loads(response.content)['access_token']
        expires_in = json.loads(response.content)['expires_in']
        expire_time = time.time() + expires_in

    return access_token




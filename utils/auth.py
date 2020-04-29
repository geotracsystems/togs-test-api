import json
import time
import requests
import utils.global_vars as g


def oauth2_token(env):
    if g.expire_time < time.time():
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
        # print(response.content)
        # print(response.status_code)
        g.access_token = json.loads(response.content)['access_token']
        expires_in = json.loads(response.content)['expires_in']
        g.expire_time = time.time() + expires_in

    return g.access_token

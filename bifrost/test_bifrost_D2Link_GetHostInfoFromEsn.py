import pytest
from utils.api_defs import bifrost
from utils.auth import oauth2_token
import json
import requests
import utils.global_vars as g


@pytest.fixture(scope='module')
def endpoint(env):
    g.access_token = ''
    g.expire_time = 0
    path = bifrost[env]['endpoint'] + '/api/D2Link/GetHostInfoFromEsn'
    return path


@pytest.fixture()
def token(env):
    oauth2 = oauth2_token(bifrost[env]['oauth'])
    return oauth2


def test_d2linkhost_invalid_header_blank(endpoint):
    header = {}
    data = {"tabletSn": "730163500077"}

    resp = requests.post(endpoint, headers=header, data=json.dumps(data))

    assert resp.status_code == 401


def test_d2linkhost_no_header(endpoint):
    data = {"tabletSn": "730163500077"}

    resp = requests.post(endpoint, data=json.dumps(data))

    assert resp.status_code == 401


def test_d2linkhost_invalid_header_notoken(endpoint):
    header = {"Content-Type": "application/json"}
    data = {"tabletSn": "730163500077"}

    resp = requests.post(endpoint, headers=header, data=json.dumps(data))

    assert resp.status_code == 401


def test_d2linkhost_invalid_header_nocontenttype(token, endpoint):
    header = {"Authorization": f"Bearer {token}"}
    data = {"tabletSn": "730163500077"}

    resp = requests.post(endpoint, headers=header, data=json.dumps(data))

    assert resp.status_code == 415


def test_d2linkhost_invalid_header_invalidtoken(endpoint):
    header = {"Content-Type": "application/json", "Authorization": f"Bearer invalidtoken123"}
    data = {"tabletSn": "730163500077"}

    resp = requests.post(endpoint, headers=header,
                         data=json.dumps(data))

    assert resp.status_code == 500
    # assert resp.status_code == 401 #Possible bug


def test_d2linkhost_invalid_body_blank(token, endpoint):
    header = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    data = {}

    resp = requests.post(endpoint, headers=header, data=json.dumps(data))

    assert resp.status_code == 500
    # assert resp.status_code == 400 #Possible bug


def test_d2linkhost_no_body(token, endpoint):
    header = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}

    resp = requests.post(endpoint, headers=header)

    assert resp.status_code == 400


def test_d2linkhost_invalid_data_type(token, endpoint):
    header = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    data = {"tablet": "730163500077"}

    resp = requests.post(endpoint, headers=header, data=json.dumps(data))

    assert resp.status_code == 500
    # assert resp.status_code == 400 #possible bug


def test_d2linkhost_invalid_data_sn(token, endpoint):
    header = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    data = {"tabletSn": "730163077"}

    resp = requests.post(endpoint, headers=header, data=json.dumps(data))
    errors = json.loads(resp.content)['ErrorMessages']

    assert (resp.status_code == 200 and len(errors) > 0)


def test_d2linkhost_valid_mdt7p(token, endpoint):
    header = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    data = {"tabletSn": "730163500077"}

    resp = requests.post(endpoint, headers=header, data=json.dumps(data))
    valid_response = json.loads(resp.content)
    errors = valid_response['ErrorMessages']

    assert (resp.status_code == 200
            and len(errors) == 0
            and valid_response['D2LinkUrl'] == 'd2link.assetcontrolcenter.com/d2link'
            and valid_response['AccountId'] == '2413'
            and valid_response['AuthCode'] == 'password'
            and valid_response['AuthUrl'] == 'http://d2link.geotracdemo.com/d2linkauth/api/login/auth')

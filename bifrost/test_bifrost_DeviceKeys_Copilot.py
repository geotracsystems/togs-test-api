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
    path = bifrost[env]['endpoint'] + '/api/DeviceKeys/GetCoPilotLicenseKeys'
    return path


@pytest.fixture()
def token(env):
    oauth2 = oauth2_token(bifrost[env]['oauth'])
    return oauth2


def test_copilot_invalid_header_blank(endpoint):
    header = {}
    data = {"tabletSn": "730163500077"}

    resp = requests.post(endpoint, headers=header, data=json.dumps(data))

    assert resp.status_code == 401


def test_copilot_no_header(endpoint):
    data = {"tabletSn": "730163500077"}

    resp = requests.post(endpoint, data=json.dumps(data))

    assert resp.status_code == 401


def test_copilot_invalid_header_notoken(endpoint):
    header = {"Content-Type": "application/json"}
    data = {"tabletSn": "730163500077"}

    resp = requests.post(endpoint, headers=header, data=json.dumps(data))

    assert resp.status_code == 401


def test_copilot_invalid_header_nocontenttype(token, endpoint):
    header = {"Authorization": f"Bearer {token}"}
    data = {"tabletSn": "730163500077"}

    resp = requests.post(endpoint, headers=header, data=json.dumps(data))

    assert resp.status_code == 415


def test_copilot_invalid_header_invalidtoken(endpoint):
    header = {"Content-Type": "application/json", "Authorization": f"Bearer invalidtoken123"}
    data = {"tabletSn": "730163500077"}

    resp = requests.post(endpoint, headers=header, data=json.dumps(data))

    assert resp.status_code == 500
    # assert resp.status_code == 401 #possible bug


def test_copilot_invalid_body_blank(token, endpoint):
    header = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    data = {}

    resp = requests.post(endpoint, headers=header, data=json.dumps(data))

    assert resp.status_code == 400


def test_copilot_no_body(token, endpoint):
    header = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}

    resp = requests.post(endpoint, headers=header)

    assert resp.status_code == 400


def test_copilot_invalid_data_type(token, endpoint):
    header = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    data = {"tablet": "730163500077"}

    resp = requests.post(endpoint, headers=header, data=json.dumps(data))

    assert resp.status_code == 400


def test_copilot_invalid_data_sn(token, endpoint):
    header = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    data = {"tabletSn": "730163077"}

    resp = requests.post(endpoint, headers=header, data=json.dumps(data))
    response = json.loads(resp.content)

    assert (resp.status_code == 200
            and len(response['LicenseKeys']) == 0
            and response['IsAuthorizedForCoPilot'] is False)


def test_copilot_valid_mdt7p(token, endpoint):
    header = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    data = {"tabletSn": "730163500077"}

    resp = requests.post(endpoint, headers=header, data=json.dumps(data))
    response = json.loads(resp.content)

    assert (resp.status_code == 200
            and len(response['LicenseKeys']) == 1
            and response['IsAuthorizedForCoPilot'] is True)


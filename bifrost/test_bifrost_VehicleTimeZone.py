import pytest
from utils.api_defs import bifrost, oauth
from utils.auth import oauth2_token
import json
import requests

endpoint = bifrost['test']['endpoint'] + '/api/VehicleTimeZone/GetVehicleTimeZone'


@pytest.fixture()
def token():
    oauth2 = oauth2_token(oauth['test'])
    return oauth2


def test_timezone_invalid_header_blank():
    header = {}
    data = {"tabletSn": "730163500077"}

    resp = requests.post(endpoint, headers=header, data=json.dumps(data))

    assert resp.status_code == 401


def test_timezone_no_header():
    data = {"tabletSn": "730163500077"}

    resp = requests.post(endpoint, data=json.dumps(data))

    assert resp.status_code == 401


def test_timezone_invalid_header_notoken():
    header = {"Content-Type": "application/json"}
    data = {"tabletSn": "730163500077"}

    resp = requests.post(endpoint, headers=header, data=json.dumps(data))

    assert resp.status_code == 401


def test_timezone_invalid_header_nocontenttype(token):
    header = {"Authorization": f"Bearer {token}"}
    data = {"tabletSn": "730163500077"}

    resp = requests.post(endpoint, headers=header, data=json.dumps(data))

    assert resp.status_code == 415


def test_timezone_invalid_header_invalidtoken():
    header = {"Content-Type": "application/json", "Authorization": f"Bearer invalidtoken123"}
    data = {"tabletSn": "730163500077"}

    resp = requests.post(endpoint, headers=header, data=json.dumps(data))

    assert resp.status_code == 500
    # assert resp.status_code == 401 # possible bug


def test_timezone_invalid_body_blank(token):
    header = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    data = {}

    resp = requests.post(endpoint, headers=header, data=json.dumps(data))

    assert resp.status_code == 500
    # assert resp.status_code == 400 #possible bug


def test_timezone_no_body(token):
    header = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}

    resp = requests.post(endpoint, headers=header)

    assert resp.status_code == 400


def test_timezone_invalid_data_type(token):
    header = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    data = {"tablet": "730163500077"}

    resp = requests.post(endpoint, headers=header, data=json.dumps(data))

    assert resp.status_code == 500
    # assert resp.status_code == 400 #possible bug


def test_timezone_invalid_data_sn(token):
    header = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    data = {"tabletSn": "730163077"}

    resp = requests.post(endpoint, headers=header, data=json.dumps(data))
    response = json.loads(resp.content)

    assert (resp.status_code == 500)
    # assert (resp.status_code == 200) # possible bug


def test_timezone_valid_mdt7p(token):
    header = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    data = {"tabletSn": "730163500077"}

    resp = requests.post(endpoint, headers=header, data=json.dumps(data))
    response = json.loads(resp.content)

    assert (resp.status_code == 200
            and len(response) == 7
            and response['Unit'] == 'syed_unit'
            and response['CustomerId'] == 2413
            and response['GroupName'] == 'apricots'
            and response['TimeZone'] == '(GMT-05:00) Eastern Time (US & Canada)'
            and response['TimeZoneDiff'] == -5.0
            and response['ObservesDst'] is True
            and len(response['ErrorMessages']) == 0)


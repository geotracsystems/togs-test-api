import pytest
from utils.api_defs import bifrost, oauth
from utils.auth import oauth2_token
import json
import requests

endpoint = bifrost['test']['endpoint'] + '/api/EldDevice/GetEFSDeviceInfo'


@pytest.fixture()
def token():
    oauth2 = oauth2_token(oauth['test'])
    return oauth2


def test_efsinfo_invalid_header_blank():
    header = {}
    data = {"tabletSn": "730163500077"}

    resp = requests.post(endpoint, headers=header, data=json.dumps(data))

    assert resp.status_code == 401


def test_efsinfo_no_header():
    data = {"tabletSn": "730163500077"}

    resp = requests.post(endpoint, data=json.dumps(data))

    assert resp.status_code == 401


def test_efsinfo_invalid_header_notoken():
    header = {"Content-Type": "application/json"}
    data = {"tabletSn": "730163500077"}

    resp = requests.post(endpoint, headers=header, data=json.dumps(data))

    assert resp.status_code == 401


def test_efsinfo_invalid_header_nocontenttype(token):
    header = {"Authorization": f"Bearer {token}"}
    data = {"tabletSn": "730163500077"}

    resp = requests.post(endpoint, headers=header, data=json.dumps(data))

    assert resp.status_code == 415


def test_efsinfo_invalid_header_invalidtoken():
    header = {"Content-Type": "application/json", "Authorization": f"Bearer invalidtoken123"}
    data = {"tabletSn": "730163500077"}

    resp = requests.post(endpoint, headers=header, data=json.dumps(data))

    assert resp.status_code == 500
    # assert resp.status_code == 401 #possible bug


def test_efsinfo_invalid_body_blank(token):
    header = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    data = {}

    resp = requests.post(endpoint, headers=header, data=json.dumps(data))

    assert resp.status_code == 404
    # assert resp.status_code == 400 #possible bug, misuse of 404


def test_efsinfo_no_body(token):
    header = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}

    resp = requests.post(endpoint, headers=header)

    assert resp.status_code == 400


def test_efsinfo_invalid_data_type(token):
    header = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    data = {"tablet": "730163500077"}

    resp = requests.post(endpoint, headers=header, data=json.dumps(data))

    assert resp.status_code == 404
    # assert resp.status_code == 400 #possible bug, incorrect use of 404


def test_efsinfo_invalid_data_sn(token):
    header = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    data = {"tabletSn": "730163077"}

    resp = requests.post(endpoint, headers=header, data=json.dumps(data))

    assert (resp.status_code == 404)
    # possible bug, misuse of 404


def test_efsinfo_valid_mdt7p(token):
    header = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    data = {"tabletSn": "730163500077"}

    resp = requests.post(endpoint, headers=header, data=json.dumps(data))
    response = json.loads(resp.content)

    assert (resp.status_code == 200
            and response['AssetUnitNumber'] == 'syed_unit'
            and len(response['CustomerInfo']) == 7
            and response['CustomerInfo']['CustomerId'] == 2413
            and response['CustomerInfo']['IsAEldCustomer'] is True
            and response['CustomerInfo']['HasAEfsProvisioningKey'] is True
            and response['CustomerInfo']['EfsProvisioningKey'] == '4NNMQWK39'
            and response['CustomerInfo']['Port'] == 4001
            and response['CustomerInfo']['HasDVIREnabled'] is False)


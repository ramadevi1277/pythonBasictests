import pytest
import requests
import json
from pytest_demo.test_api import setup_Url

def test_login_invalid(setup_Url):
    url = setup_Url + "/login/"
    data = {'email':'test@test.com', 'password':'something'}
    resp = requests.post(url, data=data)
    j = json.loads(resp.text)
    assert resp.status_code == 400
    assert j['error'] == "user not found"


def test_login_no_password(setup_Url):
	url = setup_Url + "/login/"
	data = {'email':'test@test.com'}
	resp = requests.post(url, data= data)
	j = json.loads(resp.text)
	assert resp.status_code == 400, resp.text
	assert j['error'] == "Missing password", resp.text
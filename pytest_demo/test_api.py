import pytest
import requests
import json

#### to get the data for print statements go to the folder "C:\Users\rcheepurupalli\PycharmProjects\pythonBasictests\pytest_demo"
####run pytest test_api.py -v -s
###pytest documentation link ---- https://docs.pytest.org/en/latest/contents.html

@pytest.fixture()
def setup_Url():
    return "https://reqres.in/api"

@pytest.mark.parametrize("userid, username", [(1,"George"),(2,"Janet")])
def test_list_valid_user(setup_Url, userid, username):
    url = setup_Url + "/users/" + str(userid)
    resp = requests.get(url)
    j = json.loads(resp.text)
    print(resp.text)
    assert resp.status_code == 200
    assert j["data"]['id'] == userid, resp.text
    assert j['data']['first_name'] == username, resp.text

def test_invaid_user(setup_Url):
    url = setup_Url + "/users/50"
    resp = requests.get(url)
    j = json.loads(resp.text)
    assert resp.status_code == 404, resp.text

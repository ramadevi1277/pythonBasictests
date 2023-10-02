import pytest
from selenium import webdriver

#from pytest_demo.pytest_DOM_prj.config.config import TestData

from config.config import TestData

@pytest.fixture(params=["Firefox"], scope="class")

def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.CHEOME_EXE_PATH)
    if request.param == "Firefox":
        web_driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXE_PATH)

    request.cls.driver = web_driver
    yield
    web_driver.close()


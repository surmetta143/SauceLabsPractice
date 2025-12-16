import pytest
from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def open_chrome():

    driver = webdriver.Chrome()
    return driver
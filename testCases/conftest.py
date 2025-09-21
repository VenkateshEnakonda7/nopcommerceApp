'''setup driver to reuse the method'''
import pytest
from selenium import webdriver


@pytest.fixture
def setup():
    '''
        chrome driver is initilize
    '''
    driver = webdriver.Chrome()
    return driver

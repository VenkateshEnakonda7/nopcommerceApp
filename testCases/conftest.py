'''setup driver to reuse the method'''
import pytest
from selenium import webdriver


@pytest.fixture
def setup(browser):
    '''
        chrome driver is initializing
    '''
    if browser == "chrome":
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
    else:
        driver = webdriver.Ie()
        driver.implicitly_wait(10)
    yield driver
    # driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_configure(config):
    config.metadata = {
        "Project Name": "nop Commerce",
        "Module name": "Login",
        "Tester": "Venkatesh"
    }
    config.metadata.pop("JAVA_HOME", None)
    config.metadata.pop("Plugins", None)

def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend(["Environment: QA", "Browser: Chrome"])


# @pytest.mark.optional
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)


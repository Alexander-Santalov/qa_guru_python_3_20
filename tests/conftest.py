import pytest
from selene.support.shared import browser

from fixture.application import Application
from utils import attach


@pytest.fixture()
def app(request):
    env = request.config.getoption("--env")
    fixture = Application(env)
    yield browser
    attach.add_video(browser)
    fixture.destroy()

def pytest_addoption(parser):
    parser.addoption("--env", action='store', default="android")
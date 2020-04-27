import pytest


def pytest_addoption(parser):
    parser.addoption("--env", action="store")


@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")

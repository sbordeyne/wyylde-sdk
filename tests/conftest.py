import pytest
import requests_mock

from wyylde_sdk import WyyldeClient


class MockedWyyldeClient(WyyldeClient):
    def __init__(self, *a):
        super().__init__(*a)
        

@pytest.fixture
def client():
    ...

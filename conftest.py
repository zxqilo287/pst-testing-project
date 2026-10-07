import pytest
from api_client import send_request


@pytest.fixture(scope="session")
def get_token():
    """登录，返回token；整个测试会话只执行一次"""
    res = send_request("POST", "/users/login", json_data={
        "email": "customer@practicesoftwaretesting.com",
        "password": "welcome01"
    })
    assert res.status_code == 200
    return res.json()["access_token"]

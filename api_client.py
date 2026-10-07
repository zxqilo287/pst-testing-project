import requests

BASE_URL = "https://api.practicesoftwaretesting.com"


def send_request(method, path, token=None, json_data=None, params=None):
    """公共请求方法：统一处理URL拼接、token、请求体、查询参数"""
    url = BASE_URL + path
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    session = requests.Session()
    session.trust_env = False
    response = session.request(method, url, headers=headers, json=json_data, params=params)
    return response

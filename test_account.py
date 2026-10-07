import pytest
import allure
from api_client import send_request


@pytest.mark.parametrize("email, password, expected_code", [
    ("customer@practicesoftwaretesting.com", "welcome01", 200),
    ("customer@practicesoftwaretesting.com", "wrongpass", 401),
    ("nobody@practicesoftwaretesting.com", "welcome01", 401),
])

@allure.feature("账户模块")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("验证登录")
def test_user_login(email, password, expected_code):
    """登录接口：多组数据验证"""
    res = send_request("POST", "/users/login", json_data={
        "email": email,
        "password": password
    })
    assert res.status_code == expected_code

@allure.feature("账户模块")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("获取收藏列表")
def test_query_favorite_list(get_token):
    """收藏列表接口需要token：返回200且是数组（不依赖已有数据）"""
    res = send_request("GET", "/favorites", token=get_token)
    assert res.status_code == 200
    assert isinstance(res.json(), list)

@allure.feature("账户模块")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("收藏功能验证")
def test_add_and_remove_favorite(get_token):
    """添加收藏 → 验证在列表里 → 取消收藏 → 验证被删除"""
    with allure.step("取商品列表，选一个未收藏的商品"):
        res = send_request("GET", "/products")
        products = res.json()["data"]
        res = send_request("GET", "/favorites", token=get_token)
        favorited_ids = {item["product_id"] for item in res.json()}
        product = next(p for p in products if p["id"] not in favorited_ids)
        product_id = product["id"]

    with allure.step("添加收藏"):
        res = send_request("POST", "/favorites", token=get_token, json_data={"product_id": product_id})
        assert res.status_code == 201
        favorite_id = res.json()["id"]

    with allure.step("验证收藏列表包含它"):
        res = send_request("GET", "/favorites", token=get_token)
        assert favorite_id in [item["id"] for item in res.json()]

    with allure.step("取消收藏"):
        res = send_request("DELETE", f"/favorites/{favorite_id}", token=get_token)
        assert res.status_code == 204

    with allure.step("验证收藏列表已删除"):
        res = send_request("GET", "/favorites", token=get_token)
        assert favorite_id not in [item["id"] for item in res.json()]


@allure.feature("账户模块")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("未登录状态下查看收藏")
def test_favorites_unauthorized():
    """未登录访问收藏列表返回401"""
    res = send_request("GET", "/favorites")   # 不带token
    assert res.status_code == 401

@allure.feature("账户模块")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("删除不存在收藏")
def test_delete_favorite_not_found(get_token):
    """删除不存在的收藏返回204（幂等删除）"""
    res = send_request("DELETE", "/favorites/00000000000000000000000000", token=get_token)
    assert res.status_code == 204

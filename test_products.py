import allure
from api_client import send_request


@allure.feature("商品模块")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("获取商品列表")
def test_get_product_list():
    """商品列表接口返回200，且有data字段"""
    with allure.step("发送GET请求获取商品列表"):
        res = send_request("GET", "/products")
    with allure.step("断言状态码为200"):
        assert res.status_code == 200
    with allure.step("断言响应包含data字段"):
        assert "data" in res.json()


@allure.feature("商品模块")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("获取商品详情")
def test_get_product_detail():
    """拿商品列表第一个商品ID，查它的详情"""
    with allure.step("获取商品列表"):
        res = send_request("GET", "/products")
        product_id = res.json()["data"][0]["id"]
    with allure.step("用商品ID查询详情"):
        res = send_request("GET", f"/products/{product_id}")
    with allure.step("断言状态码为200且返回name字段"):
        assert res.status_code == 200
        assert "name" in res.json()


@allure.feature("商品模块")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("搜索商品")
def test_search_product():
    """搜索商品：按名称搜索"""
    with allure.step("按关键词pliers搜索商品"):
        res = send_request("GET", "/products/search", params={"q": "pliers"})
    with allure.step("断言搜索有结果"):
        assert res.status_code == 200
        assert len(res.json()["data"]) > 0


@allure.feature("商品模块")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("查询不存在的商品返回404")
def test_get_product_not_found():
    """不存在的商品ID返回404"""
    with allure.step("请求一个不存在的商品ID"):
        res = send_request("GET", "/products/00000000000000000000000000")
    with allure.step("断言返回404"):
        assert res.status_code == 404
        assert "not found" in res.json()["message"]

# PST 测试项目

基于开源电商练习平台（practicesoftwaretesting.com）的软件测试练习项目，覆盖手工测试、接口测试、接口自动化与测试报告生成全流程。

## 项目内容

- **手工测试**：50+ 条测试用例（账号 / 商品 / 收藏 / 购物车 / 支付 / 界面）
- **接口测试**：Postman 17 个接口场景，覆盖登录、商品、收藏、购物车、支付
- **接口自动化**：pytest 11 条用例全绿，Allure 报告定制中文标题与执行步骤
- **Bug 管理**：禅道记录真实缺陷完整生命周期（发现 → 提交 → 关闭）

## 技术栈

Python · pytest · requests · Allure · Postman · 禅道

## 快速运行

```bash
pip install -r requirements.txt
pytest -v
pytest --alluredir=allure-results
allure serve allure-results

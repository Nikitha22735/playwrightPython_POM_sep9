
import allure
import pytest

from pages.home import homePage


@pytest.fixture()
def navigation(page):
    page.goto("https://www.amazon.in/")
    
@pytest.fixture()
def homePageObj(page):
    return homePage(page)


# @pytest.fixture()
# def page():
#     browser = play.chrm.launc(slowmo)
#     context = brow.newcon(viewport={})
#     page= cont.newpage

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    result = outcome.get_result()

    if result.when=="call" and result.failed :
        page = item.funcargs.get("page")
        if page:
            screenshot = page.screenshot()
            allure.attach(screenshot, name="failed screenshot", attachment_type=allure.attachment_type.PNG)

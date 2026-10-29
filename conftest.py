
import allure
from playwright.sync_api import sync_playwright
import pytest

from pages.home import homePage


@pytest.fixture()
def navigation(page):
    page.goto("https://www.amazon.in/")
    continue_button = page.get_by_role(
        "button",
        name="Continue shopping"
    )

    if continue_button.is_visible(timeout=5000):
        continue_button.click()
    
@pytest.fixture()
def homePageObj(page):
    return homePage(page)

# def page():
#     with sync_playwright() as p:
#        browser= p.chromium.launch(headless=False)
#        context = browser.new_context(geolocation={"latitude":36.778259,"longitude":-119.417931},permissions=["geolocation"])
#        page = context.new_page() 

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




@pytest.fixture(scope="session", autouse=True)
def cookieGeneration(context):
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    context.storage_state(path="testData\\cookies.json")


@pytest.fixture()
def adminpage():
    with sync_playwright() as p:
       browser= p.chromium.launch(headless=False)
       context = browser.new_context(storage_state="testData\\cookies.json")
       page = context.new_page() 
    #    if tie:
    #        cookieGeneration()
       yield page

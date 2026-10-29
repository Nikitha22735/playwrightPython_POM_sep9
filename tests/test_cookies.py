from playwright.sync_api import Page, expect, sync_playwright


# def test_cookieGeneration(context):
#     page = context.new_page()
#     page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#     page.get_by_role("textbox", name="Username").click()
#     page.get_by_role("textbox", name="Username").fill("Admin")
#     page.get_by_role("textbox", name="Password").click()
#     page.get_by_role("textbox", name="Password").click()
#     page.get_by_role("textbox", name="Password").fill("admin123")
#     page.get_by_role("button", name="Login").click()
#     context.storage_state(path="testData\\cookies.json")



def test_orange():
     with sync_playwright() as p:
           browser= p.chromium.launch(headless=False)
           context = browser.new_context(storage_state="testData\\cookies.json")
           page = context.new_page() 
           page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index") 
           page.wait_for_timeout(10000)
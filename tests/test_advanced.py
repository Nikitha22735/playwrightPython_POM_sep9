
from playwright.sync_api import sync_playwright, Playwright
import pytest

# @pytest.mark.advanced
def test_responsiveTesting():
    with sync_playwright() as p:
       browser= p.chromium.launch(headless=False)
       context = browser.new_context(viewport={"width":400, "height":200})
       page = context.new_page() 
       page.goto("https://testautomationpractice.blogspot.com/") 
       page.wait_for_timeout(3000)



# @pytest.mark.advanced
def test_mobileEmulationTesting():
    with sync_playwright() as p:
       browser= p.chromium.launch(headless=False)
       print(p.devices["iPhone XR"])
       context = browser.new_context(**p.devices["iPhone XR"])
    #    context = browser.new_context(viewport={"width":414, "height":896}, is_mobile=True, has_touch= True)
       page = context.new_page() 
       page.goto("https://testautomationpractice.blogspot.com/") 
       page.wait_for_timeout(3000)




def test_geoLocationTesting():
    with sync_playwright() as p:
       browser= p.chromium.launch(headless=False)
       context = browser.new_context(geolocation={"latitude":36.778259,"longitude":-119.417931},permissions=["geolocation"])
       page = context.new_page() 
       page.goto("https://browserleaks.com/geo") 
       page.wait_for_timeout(13000)


@pytest.mark.advanced
def test_offlineTesting():
    with sync_playwright() as p:
       browser= p.chromium.launch(headless=False)
       context = browser.new_context()
       page = context.new_page() 
       page.goto("https://testautomationpractice.blogspot.com/") 
       context.set_offline(True)
       page.get_by_text("Udemy Courses").click()
       context.set_offline(False)
       page.wait_for_timeout(13000)
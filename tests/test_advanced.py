
import io

import allure
from playwright.sync_api import sync_playwright, Playwright, expect
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


# @pytest.mark.advanced
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

@pytest.mark.advanced
def test_visualtesting():
    with sync_playwright() as p:
      browser= p.chromium.launch(headless=False)
      context = browser.new_context()
      page = context.new_page() 
      page.goto("https://www.facebook.com/") 
      # page.screenshot(path="screenshots/ss3.png")
      expect.soft(page.get_by_text("Log in2")).to_be_visible()
      print("hello")

from PIL import Image, ImageChops
# @pytest.mark.advanced
def test_visualtesting2():
   ss1_path = "screenshots\\ss1.png"
   ss2_path = "screenshots\\ss2.png"
   allure.attach.file(ss1_path, name="ss1", attachment_type=allure.attachment_type.PNG)
   allure.attach.file(ss2_path, name="ss2", attachment_type=allure.attachment_type.PNG)

   pix1 = Image.open(ss1_path)
   pix2 = Image.open(ss2_path)
   diff = ImageChops.difference(pix1, pix2)
   mask = ImageChops.lighter(
      ImageChops.lighter(diff.getchannel("R"), diff.getchannel("G")),
      diff.getchannel("B"),
   ).point(lambda value: 255 if value else 0)
   highlighted = pix1.convert("RGBA")
   red_overlay = Image.new("RGBA", pix1.size, (255, 0, 0, 0))
   red_overlay.putalpha(mask)
   highlighted = Image.alpha_composite(highlighted, red_overlay)

   diff_image = io.BytesIO()
   highlighted.save(diff_image, format="PNG")
   allure.attach(
      diff_image.getvalue(),
      name="visual diff (changed pixels in red)",
      attachment_type=allure.attachment_type.PNG,
   )

   assert diff.getbbox() is None, "ss are diff"

      

from playwright.sync_api import Page, expect
import pytest

from pages.home import homePage

@pytest.mark.smoke
@pytest.mark.home
def test_HomeScreenUI(adminpage: Page, navigation):
    homePageObj = homePage(adminpage)
    adminpage.wait_for_timeout(3000)
    homePageObj.validateTheVisibilityOfAmazon()
    homePageObj.validateTheVisibilityOfSearchBox()
    homePageObj.validateTheVisibilityOfCartIcon()
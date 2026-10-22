from playwright.sync_api import Page, expect
import pytest

from pages.home import homePage

@pytest.mark.smoke
def test_HomeScreenUI(page: Page, navigation):
    homePageObj = homePage(page)
    page.wait_for_timeout(3000)
    homePageObj.validateTheVisibilityOfAmazon()
    homePageObj.validateTheVisibilityOfSearchBox()
    homePageObj.validateTheVisibilityOfCartIcon()
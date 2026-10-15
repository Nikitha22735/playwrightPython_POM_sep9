from playwright.sync_api import Page, expect
import pytest

from pages.home import homePage

@pytest.mark.smoke
def test_HomeScreenUI(page: Page, navigation):
    homePageObj = homePage(page)
    homePageObj.validateTheVisibilityOfAmazon()
    homePageObj.validateTheVisibilityOfSearchBox()
    homePageObj.validateTheVisibilityOfCartIcon()
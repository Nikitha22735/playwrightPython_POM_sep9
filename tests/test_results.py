from playwright.sync_api import Page, expect
import pytest

from pages.authorisation import authorisationPage
from pages.home import homePage
from pages.results import resultsPage

@pytest.mark.smoke
def test_resultsScreenUI(page: Page, navigation,homePageObj):
    resultsPageObj = resultsPage(page)
    # authorisationPageObj = authorisationPage()
    # authorisationPageObj.sign_in()
    homePageObj.fillSearchData()
    homePageObj.clickOnSearchBtn()
    resultsPageObj.validateTheVisibilityOfresultsText()
    resultsPageObj.validateTheVisibilityOfFreeDeliveryText()
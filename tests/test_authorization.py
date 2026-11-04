import os

import pytest
from playwright.sync_api import Page

from pages.authorisation import authorisationPage
from utils.jsonHandling import jsonhandling


@pytest.mark.smoke

def test_positive_login(page: Page, navigation):
    credentials = jsonhandling("testData\\creds.json")
    username = credentials["positiveCreds"]["username"]
    password = credentials["positiveCreds"]["password"]
    authorization_page = authorisationPage(page)
    authorization_page.sign_in(username, password)
    # page.pause()
    authorization_page.validateSuccessfulLogin()


@pytest.mark.regression
def test_invalid_username_shows_error(page: Page, navigation):
    authorization_page = authorisationPage(page)
    authorization_page.submit_username("invalid-username")
    authorization_page.validate_invalid_username()
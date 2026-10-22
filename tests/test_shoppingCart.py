import re
from playwright.sync_api import Page, expect, sync_playwright
import pytest

@pytest.fixture(scope="session")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page= context.new_page()
        yield page

def test_home(page) -> None:
    page.goto("https://www.amazon.in/")
    page.get_by_role("searchbox", name="Search Amazon.in").click()
    expect(page.get_by_role("searchbox", name="Search Amazon.in")).to_be_visible()


def test_results(page):
    page.get_by_role("searchbox", name="Search Amazon.in").fill("iphone")
    page.locator('#nav-search-submit-button').click()
    expect(page.get_by_role("heading", name="Results", exact=True)).to_be_visible()
    page.locator("#a-autoid-1").get_by_role("button", name="Add to cart").click()
    page.get_by_role("link", name="item in cart").click()

def test_shopping(page):
    expect(page.get_by_role("heading", name="Shopping Cart")).to_be_visible()

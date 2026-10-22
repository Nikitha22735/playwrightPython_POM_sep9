import allure
from playwright.sync_api import Page, expect
class homePage:
    # searchBox = page.get_by_role("searchbox", name="Search Amazon.in")

    def __init__(self,page):
        self.searchBox = page.get_by_role("searchbox", name="Search Amazon.in")
        self.amazonLogo = page.get_by_role("link", name="Amazon.in")
        self.cartIcon = page.get_by_role("link", name="items in cart")
        self.searchbtn =  page.locator('#nav-search-submit-button')

    @allure.step('validateTheVisibilityOfSearchBox')
    def validateTheVisibilityOfSearchBox(self):
        expect(self.searchBox).to_be_visible()

    @allure.step('validateTheVisibilityOfAmazon')
    def validateTheVisibilityOfAmazon(self):
        expect(self.amazonLogo).not_to_be_visible()

    @allure.step('validateTheVisibilityOfCartIcon')
    def validateTheVisibilityOfCartIcon(self):
        expect(self.cartIcon).to_be_visible()

    @allure.step('fillSearchData')
    def fillSearchData(self):
        self.searchBox.fill("iphone")

    @allure.step('clickOnSearchBtn')
    def clickOnSearchBtn(self):
        self.searchbtn.click()
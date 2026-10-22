import allure
from playwright.sync_api import Page, expect


class authorisationPage:
    def __init__(self, page: Page) -> None:
        self.accountListsLink = page.get_by_role(
            "link", name="Hello, sign in Account & Lists"
        )
        self.usernameTextbox = page.get_by_role(
            "textbox", name="Enter mobile number or email"
        )
        self.continueButton = page.get_by_role("button", name="Continue")
        self.usernameError = page.get_by_role("alert")
        self.passwordTextbox = page.get_by_role("textbox", name="Password")
        self.signInButton = page.get_by_role("button", name="Sign in")
        self.searchBox = page.get_by_role("searchbox", name="Search Amazon.in")

    @allure.step('submit_username')
    def submit_username(self, username: str) -> None:
        self.accountListsLink.click()
        self.usernameTextbox.fill(username)
        self.continueButton.click()

    @allure.step('sign_in')
    def sign_in(self, username: str, password: str) -> None:
        self.submit_username(username)
        self.passwordTextbox.fill(password)
        self.signInButton.click()

    @allure.step('validateSuccessfulLogin')
    def validateSuccessfulLogin(self) -> None:
        expect(self.searchBox).to_be_visible()

    @allure.step('validate_invalid_username')
    def validate_invalid_username(self) -> None:
        expect(self.usernameError).to_have_text("Invalid email address")
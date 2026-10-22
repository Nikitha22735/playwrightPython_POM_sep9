
import allure
from playwright.sync_api import Page, expect

class resultsPage:
    def __init__(self, page):
        self.resultsText = page.get_by_role("heading", name="Results", exact=True)
        self.freeDeliverytext = page.get_by_text("Eligible for Free Delivery")

    @allure.step('validateTheVisibilityOfresultsText')
    def validateTheVisibilityOfresultsText(self):
            expect(self.resultsText).to_be_visible()

    @allure.step('validateTheVisibilityOfFreeDeliveryText')
    def validateTheVisibilityOfFreeDeliveryText(self):
        expect(self.freeDeliverytext).to_be_visible()
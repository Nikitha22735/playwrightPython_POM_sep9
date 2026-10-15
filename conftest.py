
import pytest

from pages.home import homePage


@pytest.fixture()
def navigation(page):
    page.goto("https://www.amazon.in/")
    
@pytest.fixture()
def homePageObj(page):
    return homePage(page)


# @pytest.fixture()
# def page():
#     browser = play.chrm.launc(slowmo)
#     context = brow.newcon(viewport={})
#     page= cont.newpage

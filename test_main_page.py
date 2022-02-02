import pytest

from .pages.main_page import MainPage


@pytest.mark.login_guest
class TestLoginFromMainPage:
    link = "http://selenium1py.pythonanywhere.com"

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, self.link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, self.link)
        page.open()
        page.should_be_login_link()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = MainPage(browser, self.link)
        page.open()
        page.go_to_basket_page()
        page.should_be_basket_is_empty_text()
        page.should_be_basket_is_empty_product()

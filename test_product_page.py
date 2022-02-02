import time
import pytest

from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
promo_parts = ["?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3", "?promo=offer4", "?promo=offer5",
               "?promo=offer6", pytest.param("?promo=offer7", marks=pytest.mark.xfail), "?promo=offer8",
               "?promo=offer9"]


@pytest.mark.need_review
@pytest.mark.parametrize("link_parts", promo_parts)
def test_guest_can_add_product_to_basket(browser, link_parts):
    link_par = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{link_parts}"
    page = ProductPage(browser, link_par)
    page.open()
    page.should_be_product_page()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_basket_is_empty_text()
    page.should_be_basket_is_empty_product()


class TestUserAddToBasketFromProductPage:
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = None

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.page = ProductPage(browser, self.link)
        self.page.open()
        self.page.go_to_login_page()
        email = str(time.time()) + "@fakemail.ru"
        password = "SeleniumWaiver"
        self.page.register_new_user(email, password)
        self.page.should_be_authorized_user()
        self.page.go_to_recommended_reading_link()

    def test_user_cant_see_success_message(self):
        self.page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self):
        self.page.should_be_product_page()

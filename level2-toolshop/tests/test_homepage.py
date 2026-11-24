
from playwright.sync_api import expect


def test_homepage_loads(page, base_url):
    page.goto(base_url)

    expect(page.locator('[data-test="search-query"]')).to_be_visible()


def test_search_button_is_visible(page, base_url):
    page.goto(base_url)

    expect(page.locator('[data-test="search-submit"]')).to_be_visible()

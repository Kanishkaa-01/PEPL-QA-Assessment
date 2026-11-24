
from playwright.sync_api import expect


def test_search_input_is_visible(page, base_url):
    page.goto(base_url)

    search_input = page.locator(
        '[data-test="search-query"]'
    )

    expect(search_input).to_be_visible()


def test_search_for_pliers(page, base_url):
    page.goto(base_url)

    search_input = page.locator(
        '[data-test="search-query"]'
    )

    search_input.fill("Pliers")

    page.locator(
        '[data-test="search-submit"]'
    ).click()

    product_names = page.locator(
        '[data-test="product-name"]'
    )

    expect(product_names.first).to_be_visible()
    assert product_names.count() > 0


def test_search_for_nonexistent_product(page, base_url):
    page.goto(base_url)

    search_input = page.locator(
        '[data-test="search-query"]'
    )

    search_input.fill("XYZNonexistentProduct123")

    page.locator(
        '[data-test="search-submit"]'
    ).click()

    expect(
        page.get_by_text(
            "0 products found",
            exact=False
        )
    ).to_be_visible(timeout=10000)
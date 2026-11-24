from playwright.sync_api import expect


def test_products_are_displayed(page, base_url):
    page.goto(base_url)

    products = page.locator(
        '[data-test="product-name"]'
    )

    expect(products.first).to_be_visible()

    assert products.count() > 0


def test_product_names_are_not_empty(page, base_url):
    page.goto(base_url)

    products = page.locator(
        '[data-test="product-name"]'
    )

    expect(products.first).to_be_visible()

    for index in range(products.count()):
        name = products.nth(index).inner_text()
        assert name.strip() != "", (
            f"Product at position {index} has an empty name"
        )

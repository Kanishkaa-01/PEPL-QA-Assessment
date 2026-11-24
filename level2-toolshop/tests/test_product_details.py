from playwright.sync_api import Page, expect


def test_product_details_page_opens(page: Page, base_url):
    page.goto(
        base_url,
        wait_until="domcontentloaded",
        timeout=60000
    )

    first_product = page.locator("a.card").first

    product_name = first_product.locator(
        '[data-test="product-name"]'
    ).inner_text()

    first_product.click()

    product_heading = page.locator(
        '[data-test="product-name"]'
    )

    expect(product_heading).to_be_visible()

    expect(product_heading).to_contain_text(
        product_name.strip()
    )
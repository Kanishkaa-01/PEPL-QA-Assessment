
from playwright.sync_api import Page, expect


def test_add_product_to_cart(page: Page, base_url):
    # Open the website
    page.goto(
        base_url,
        wait_until="domcontentloaded",
        timeout=60000
    )

    # Open the first available product
    first_product = page.locator("a.card").first
    expect(first_product).to_be_visible()

    first_product.click()

    # Capture the product name
    product_name = page.locator('[data-test="product-name"]')
    expect(product_name).to_be_visible()
    name = product_name.inner_text()

    # Locate the Add to Cart button
    add_to_cart = page.locator('[data-test="add-to-cart"]')
    expect(add_to_cart).to_be_visible()

    # Capture screenshot evidence before clicking
    page.screenshot(
        path="screenshots/cart-add-button-disabled.png",
        full_page=True
    )

    # Attempt to add the product to the cart
    add_to_cart.click()

    # Open the cart
    page.locator('[data-test="nav-cart"]').click()

    # Verify that the selected product appears in the cart
    expect(page.get_by_text(name, exact=True)).to_be_visible()


def test_update_product_quantity(page: Page, base_url):
    page.goto(
        base_url,
        wait_until="domcontentloaded",
        timeout=60000
    )

    # Open the first product
    page.locator("a.card").first.click()

    # Add product to cart
    page.locator('[data-test="add-to-cart"]').click()

    # Open cart
    page.locator('[data-test="nav-cart"]').click()

    # Update quantity
    quantity = page.locator('[data-test="product-quantity"]')
    expect(quantity).to_be_visible()
    quantity.fill("2")

    # Verify updated quantity
    expect(quantity).to_have_value("2")


def test_remove_product_from_cart(page: Page, base_url):
    page.goto(
        base_url,
        wait_until="domcontentloaded",
        timeout=60000
    )

    # Open the first product
    page.locator("a.card").first.click()

    # Add product to cart
    page.locator('[data-test="add-to-cart"]').click()

    # Open cart
    page.locator('[data-test="nav-cart"]').click()

    # Remove product
    page.locator("a.btn.btn-danger").click()

    # Verify cart is empty
    expect(
        page.get_by_text("The cart is empty. Nothing to display.")
    ).to_be_visible()

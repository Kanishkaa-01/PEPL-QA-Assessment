
import pytest
from playwright.sync_api import Page, expect


@pytest.mark.parametrize("sort_value, sort_type", [
    ("name,asc", "name"),
    ("name,desc", "name"),
    ("price,asc", "price"),
    ("price,desc", "price"),
])


def test_product_sorting(
    page: Page,
    base_url,
    sort_value,
    sort_type
):
    page.goto(base_url, wait_until="domcontentloaded", timeout=60000)

    sort_dropdown = page.locator('[data-test="sort"]')
    sort_dropdown.select_option(sort_value)

    expect(sort_dropdown).to_have_value(sort_value)

    page.wait_for_timeout(2000)

    if sort_type == "name":
        elements = page.locator('[data-test="product-name"]')
        values = elements.all_inner_texts()
        actual = [value.strip().lower() for value in values]

    else:
        elements = page.locator('[data-test="product-price"]')
        values = elements.all_inner_texts()
        actual = [
            float(value.replace("$", "").strip())
            for value in values
        ]

    expected = sorted(
        actual,
        reverse=sort_value.endswith("desc")
    )

    assert actual == expected, (
        f"Sorting failed for {sort_value}. Actual: {actual}"
    )

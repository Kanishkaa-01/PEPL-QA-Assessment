from playwright.sync_api import Page, expect


def test_contact_form_fields_are_visible(page: Page, base_url):
    page.goto(base_url)
    page.locator('[data-test="nav-contact"]').click()

    expect(page.locator('[data-test="first-name"]')).to_be_visible()
    expect(page.locator('[data-test="last-name"]')).to_be_visible()
    expect(page.locator('[data-test="email"]')).to_be_visible()
    expect(page.locator('[data-test="subject"]')).to_be_visible()
    expect(page.locator('[data-test="message"]')).to_be_visible()
    expect(page.locator('[data-test="attachment"]')).to_be_visible()
    expect(page.locator('[data-test="contact-submit"]')).to_be_visible()


def test_contact_form_successful_submission(page: Page, base_url):
    page.goto(base_url)
    page.locator('[data-test="nav-contact"]').click()

    page.locator('[data-test="first-name"]').fill("Test")
    page.locator('[data-test="last-name"]').fill("User")
    page.locator('[data-test="email"]').fill("testuser@example.com")
    page.locator('[data-test="subject"]').select_option("customer-service")
    page.locator('[data-test="message"]').fill(
        "This is a test message for contact form validation."
    )

    page.locator('[data-test="contact-submit"]').click()

    page.screenshot(
        path="screenshots/contact-subject-required-error.png",
        full_page=True
    )

    expect(page.get_by_text("Thanks for your message")).to_be_visible()


def test_contact_form_required_fields(page: Page, base_url):
    page.goto(base_url)
    page.locator('[data-test="nav-contact"]').click()

    page.locator('[data-test="contact-submit"]').click()

    expect(page.locator('[data-test="first-name"]')).to_be_visible()
    expect(page.locator('[data-test="last-name"]')).to_be_visible()
    expect(page.locator('[data-test="email"]')).to_be_visible()
    expect(page.locator('[data-test="subject"]')).to_be_visible()
    expect(page.locator('[data-test="message"]')).to_be_visible()

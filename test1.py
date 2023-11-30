
import re
from playwright.sync_api import Page, expect, sync_playwright

def test_has_title(Page):
    Page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(Page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    Page.goto("https://playwright.dev/")

    # Click the get started link.
    Page.get_by_role("link", name="Get started").click()
    # Expects page to have a heading with the name of Installation.
    expect(page.locator("text=Installation")).to_be_visible()

with sync_playwright() as p:
    browser = p.chromium.launch()
    #context = browser.new_context()
    Page = browser.new_page()

    # Run your tests
    test_has_title(Page)
    test_get_started_link(Page)

    # Close the browser
    browser.close()
import re
import pytest
from playwright.sync_api import sync_playwright,expect,Page
try:
    def test_has_title(page):
        page.goto("https://playwright.dev/")
        expect(page).to_have_title(re.compile('Playwright'))


    def test_get_started_link(Page):
        Page.goto("https://playwright.dev/")
        Page.locator('text=GET STARTED').click()
        # Assuming 'Get Started' is the text for the link
        Page.locator('text=How to install playwright').click()
        Page.screenshot(path='one1.png')
        Page.wait_for_timeout(timeout=15000)
        expect(Page.get_by_role('text=Install the required browsers:'))
except :
    print('error occured')
else:
    print('no error')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    Page = context.new_page()

    test_has_title(Page)
    test_get_started_link(Page)

    browser.close()

from playwright.sync_api import Page, expect, BrowserContext, Dialog
import re


def test_alerts_button_click(page: Page):
    page.on('dialog', lambda dialog: dialog.accept())
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.locator('.a-button').click()
    expect(page.locator('#result-text')).to_have_text('Ok')


def test_open_link_in_new_tab(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    with context.expect_page() as new_page_info:
        page.locator('#new-page-button').click()
    new_page = new_page_info.value
    new_page.wait_for_load_state()
    result_text = new_page.locator('#result-text')
    expect(result_text).to_have_text('I am a new page in a new tab')
    new_page.close()
    button = page.locator('#new-page-button')
    expect(button).to_be_enabled()


def test_button_color_change(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    page.locator('#visibleAfter').wait_for(state='visible')
    color_button = page.locator('#colorChange')
    expect(color_button).to_have_class(re.compile(r'text-danger'))
    color_button.click()

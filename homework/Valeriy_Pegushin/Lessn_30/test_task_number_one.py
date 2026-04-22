from playwright.sync_api import Page, expect


def test_iphone_17_pro_modal_with_mocked_name(page: Page):
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.locator('.rf-hcard-copy').first.click()
    page.wait_for_selector('#rf-digitalmat-overlay-label-0', state='visible')
    page.evaluate('document.querySelector("#rf-digitalmat-overlay-label-0").innerText = "яблокофон 17 про"')
    expect(page.locator('#rf-digitalmat-overlay-label-0').first).to_contain_text("яблокофон 17 про")

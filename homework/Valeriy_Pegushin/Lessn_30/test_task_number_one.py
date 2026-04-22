from playwright.sync_api import Page, expect


def test_iphone_17_pro_modal_with_mocked_name(page: Page):
    def modify_real_response(route):
        response = route.fetch()
        text = response.text()
        modified_text = text.replace("iPhone\u00A017\u00A0Pro", "яблокофон 17 про")
        route.fulfill(
            status=200,
            content_type="application/json",
            body=modified_text
        )
    page.route("**/api/digital-mat**", modify_real_response)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.locator('.rf-hcard-copy').first.click()
    page.wait_for_selector('#rf-digitalmat-overlay-label-0', state='visible')
    expect(page.locator('#rf-digitalmat-overlay-label-0').first).to_contain_text("яблокофон 17 про")

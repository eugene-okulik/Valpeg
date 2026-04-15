from playwright.sync_api import Page, expect, Request, Response
import re


def test_iphone_17_pro_modal_with_mocked_name(page: Page):
    def handle_route(route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['productName'] = "яблокофон 17 про"
        route.fulfill(
            status=response.status,
            headers=response.headers,
            json=body
        )
    page.route(re.compile('digital-mat'), handle_route)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.locator('.rf-hcard-copy').locator('nth=0').click()
    modal_header = page.locator('#rf-digitalmat-overlay-label-0').locator('nth=0')
    expect(modal_header).to_contain_text("яблокофон 17 про")



from playwright.sync_api import Page, expect


def test_form_authentication(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    page.get_by_role('textbox', name='Username').fill('Valpeg')
    page.get_by_role('textbox', name='Password').fill('Valpeg19711603')
    page.get_by_role('button', name='Login').click()
    expect(page.get_by_text('Your username is invalid!')).to_be_visible()


def test_practice_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    page.locator('//input[@id="firstName"]').fill("Валерий")
    page.locator('//input[@id="lastName"]').fill("Пегушин")
    page.locator('//input[@id="userEmail"]').fill("valpegushin@yandex.ru")
    page.locator('//input[@id="gender-radio-1"]').click()
    page.locator('//input[@id="userNumber"]').fill("9128844779")
    page.locator('#dateOfBirthInput').click()
    page.locator('.react-datepicker__year-select').select_option('1971')
    page.locator('.react-datepicker__month-select').select_option('2')
    page.locator('.react-datepicker__day:has-text("16")').click()
    page.locator('#subjectsInput').fill('Computer Science')
    page.keyboard.press('Enter')
    page.keyboard.press('Escape')
    page.locator('#hobbies-checkbox-1').click()
    page.locator('#currentAddress').fill("ул. Лунная, 18")
    page.locator('#state').click()
    page.get_by_text('NCR', exact=True).click()
    page.locator('#city').click()
    page.get_by_text('Delhi', exact=True).click()
    page.locator('#submit').click()
    expect(page.locator('.modal-title')).to_have_text('Thanks for submitting the form')

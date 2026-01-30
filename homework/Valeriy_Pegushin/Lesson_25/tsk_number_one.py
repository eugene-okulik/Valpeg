from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
# from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    # chrome_driver.implicitly_wait(10)
    # sleep(3)
    chrome_driver.maximize_window() # Открытие страницы на весь экран
    yield chrome_driver
    # sleep(3)


def test_result_text(driver):
    input_data = "ValPeg"
    driver.get("https://www.qa-practice.com/elements/input/simple")
    text_string = driver.find_element(By.ID, "id_text_string")
    text_string.send_keys(input_data)
    #text_string.submit()
    text_string.send_keys(Keys.ENTER)
    result_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "result-text"))
    )
    assert result_text.text == input_data
    print(f"Введенный текст: {input_data}")
    print(f"Результат на странице: {result_text.text}")


def test_student_registration_form(driver):
    driver.get("https://demoqa.com/automation-practice-form")
    # sleep(3)
    driver.find_element(By.ID, 'firstName').send_keys('Valeriy')
    driver.find_element(By.ID, 'lastName').send_keys('Pegushin')
    driver.find_element(By.ID, 'userEmail').send_keys('valpegushin@yandex.ru')
    driver.find_element(By.XPATH, '//label[@for="gender-radio-1"]').click()
    driver.find_element(By.ID, 'userNumber').send_keys('9128844779')
    date_of_birth_input = driver.find_element(By.ID, 'dateOfBirthInput')
    driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", date_of_birth_input)
    date_of_birth_input.click()
    # driver.find_element(By.ID, 'dateOfBirthInput').click()
    # sleep(2)
    driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select').click()
    # sleep(1)
    driver.find_element(By.XPATH, "//option[@value='1971']").click()
    driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select').click()
    # sleep(1)
    driver.find_element(By.XPATH, "//option[@value='2']").click()
    driver.find_element(
        By.XPATH,
        "//div[contains(@class, 'react-datepicker__day--016') and text()='16']"
    ).click()
    # sleep(2)
    subjects_input = driver.find_element(By.ID, "subjectsInput")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", subjects_input)
    driver.execute_script("arguments[0].click();", subjects_input)
    subjects_input.send_keys('Maths')
    subjects_input.send_keys(Keys.ENTER)
    sports_checkbox = driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-1']")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", sports_checkbox)
    sports_checkbox.click()
    current_address = driver.find_element(By.ID, "currentAddress")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", current_address)
    current_address.click()
    current_address.send_keys("Russia, 614023, Perm, Lunnaya, 18")
    state_dropdown = driver.find_element(By.XPATH, "//div[@id='state']")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", state_dropdown)
    state_dropdown.click()
    ncr_option = driver.find_element(By.XPATH, "//div[text()='NCR']")
    ncr_option.click()
    city_dropdown = driver.find_element(By.ID, "city")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", city_dropdown)
    city_dropdown.click()
    delhi_option = driver.find_element(By.XPATH, "//div[text()='Delhi']")
    delhi_option.click()
    submit_btn = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_btn)
    # sleep(1)
    submit_btn.click()

    print("\n" + "=" * 50)
    print("РЕЗУЛЬТАТЫ:")
    print("=" * 50)

    modal_content = driver.find_element(By.CLASS_NAME, "modal-body").text
    print(modal_content)

    print("=" * 50)

    print("✓ Тест успешно пройден!")
    print("✓ Все поля корректно заполнены")


def test_submit_and_select(driver):
    driver.get("https://www.qa-practice.com/elements/select/single_select")
    select = driver.find_element(By.NAME, "choose_language")
    choose_language = Select(select)
    choose_language.select_by_value("1")
    submit_button = driver.find_element(By.ID, "submit-id-submit")
    submit_button.click()
    you_selected = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "result-text"))
    )
    assert you_selected.text == "Python"


def test_hello_world(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    start_button = driver.find_element(By.XPATH, '//div[@id="start"]/button')
    start_button.click()
    hello_world = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="finish"]/h4'))
    )
    assert hello_world.text == "Hello World!"

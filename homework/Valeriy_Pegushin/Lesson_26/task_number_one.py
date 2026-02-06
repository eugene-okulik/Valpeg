from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest
# from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    # chrome_driver.implicitly_wait(10)
    # sleep(3)
    chrome_driver.maximize_window()  # Открытие страницы на весь экран
    yield chrome_driver
    # sleep(3)


def test_new_tab (driver):
    driver.get('http://testshop.qa-practice.com/')
    expected_product = "Customizable Desk"
    print(f"Добавляем товар: {expected_product}")
    product_image = driver.find_element(By.XPATH,"//img[@alt='Customizable Desk']")
    actions = ActionChains(driver)
    actions.key_down(Keys.COMMAND).click(product_image).key_up(Keys.COMMAND).perform()
    # sleep(3)
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    # sleep(3)
    add_to_cart = driver.find_element(By.ID, "add_to_cart")
    add_to_cart.click()
    # sleep(3)
    continue_shopping = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-secondary']"))
    )
    continue_shopping.click()
    # sleep(3)
    driver.close()
    # sleep(3)
    driver.switch_to.window(tabs[0])
    # sleep(3)
    driver.refresh()
    # sleep(3)
    wait = WebDriverWait(driver, 10)
    second_cart_link = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//i[contains(@class, 'fa-shopping-cart')]/ancestor::a)[1]"))
    )
    second_cart_link.click()
    # sleep(3)
    cart_product_name = driver.find_element(
        By.XPATH,"//h6[contains(@class, 'h6') and contains(text(), 'Customizable Desk')]"
    ).text
    print(f"✓ Товар в корзине: {cart_product_name}")
    assert expected_product in cart_product_name, f"Ожидался '{expected_product}', найден '{cart_product_name}'"


def test_cart_button(driver):
    driver.get('http://testshop.qa-practice.com/')
    product_image = driver.find_element(By.XPATH, "//img[@alt='Customizable Desk']")
    actions = ActionChains(driver)
    actions.move_to_element(product_image).perform()
    # sleep(3)
    cart_button = driver.find_element(
        By.XPATH, "(//a[@class='btn btn-primary a-submit' and @title='Shopping cart'])[1]"
    )
    cart_button.click()
    # sleep(3)
    product_element = driver.find_element(
        By.XPATH, "(//strong[@class='product-name product_display_name'])[1]"
    )
    print(f"Товар: {product_element.text}")









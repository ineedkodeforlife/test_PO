import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def main_menu(title_text):
    if title_text.text == "Products":
        print("Мы попали на главную страницу")
    else:
        print("Ошибка поиска элемента")


def first_test():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # Поиск элементов и присваивание к переменным.
    input_username = driver.find_element("xpath", "//*[@id=\"user-name\"]")
    input_password = driver.find_element("xpath","//*[@id=\"password\"]")
    login_button = driver.find_element("xpath","//*[@id=\"login-button\"]")

    # Действия с формами
    input_username.send_keys("standard_user")
    input_password.send_keys("secret_sauce")
    login_button.send_keys(Keys.RETURN)

    # Поиск и проверка попадания на главную страницу
    title_text = driver.find_element("xpath", "//*[@id=\"header_container\"]/div[2]/span")
    main_menu(title_text)

    time.sleep(5)

    driver.find_element("xpath", '//*[@id="shopping_cart_container"]/a').click()

    text_shopping_basket = driver.find_element("xpath", '//*[@id="header_container"]/div[2]/span')
    if text_shopping_basket.text == "Your Cart":
        print("Мы попали в корзину")
    else:
        print("Ошибка поиска элемента")
    time.sleep(5)

    driver.find_element("xpath", '//*[@id="continue-shopping"]').click()
    title_text = driver.find_element("xpath", "//*[@id=\"header_container\"]/div[2]/span")
    main_menu(title_text)

    time.sleep(5)

    driver.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    time.sleep(2)
    driver.find_element("xpath", '//*[@id="shopping_cart_container"]/a').click()
    time.sleep(2)

    name_of_product = driver.find_element('xpath', '//*[@id="item_4_title_link"]/div')
    if name_of_product.text == 'Sauce Labs Backpack':
        print('Мы добавили элемент в корзину')
    else:
        print('Ошибка поиска')
    time.sleep(5)


if __name__ == '__main__':
    first_test()

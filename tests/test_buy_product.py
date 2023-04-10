import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page


@pytest.mark.run(order=3)
def test_buy_product_1():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\stati\\PycharmProjects\\webdriver\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)

    print('Start Test 1')

    login = Login_page(driver)
    login.autorization()

    item_mp = Main_page(driver)
    item_mp_text = item_mp.save_name_product_1()

    mp = Main_page(driver)
    mp.select_products_1()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    cip = Client_information_page(driver)
    cip.input_information()

    item_cp = Client_information_page(driver)
    item_cp_text = item_cp.save_cart_name_product_1()

    check_item = Base(driver)
    check_item.assert_name_product(item_mp_text, item_cp_text)
    #
    # f = Finish_page(driver)
    # f.finish()

    print('Finish Test 1')
    print('item_mp' + item_mp_text)
    print('item_cp' + item_cp_text)
    # print('Finish Test 1')
    # time.sleep(3)
    # driver.quit()

# @pytest.mark.run(order=1)
# def test_buy_product_2():
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option("detach", True)
#     g = Service('C:\\Users\\stati\\PycharmProjects\\webdriver\\chromedriver.exe')
#     driver = webdriver.Chrome(options=options, service=g)
#
#     print('Start Test 2')
#
#     login = Login_page(driver)
#     login.autorization()
#
#     mp = Main_page(driver)
#     mp.select_products_2()
#
#     cp = Cart_page(driver)
#     cp.click_checkout_button()
#
#     print('Finish Test 2')
#     time.sleep(3)
#     driver.quit()

# @pytest.mark.run(order=2)
# def test_buy_product_3():
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option("detach", True)
#     g = Service('C:\\Users\\stati\\PycharmProjects\\webdriver\\chromedriver.exe')
#     driver = webdriver.Chrome(options=options, service=g)
#
#     print('Start Test 3')
#
#     login = Login_page(driver)
#     login.autorization()
#
#     mp = Main_page(driver)
#     mp.select_products_3()
#
#     cp = Cart_page(driver)
#     cp.click_checkout_button()
#
#     print('Finish Test 3')
#     time.sleep(3)
#     driver.quit()





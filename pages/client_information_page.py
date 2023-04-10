

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from pages.main_page import Main_page


class Client_information_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    first_name = "//input[@id='first-name']"
    last_name = "//input[@id='last-name']"
    postal_code = "//input[@id='postal-code']"
    continue_button = "//input[@id='continue']"
    cart_name_product_1 = "//*[@id='item_4_title_link']/div"


    # Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_postal_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.postal_code)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    # Actoins

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print('Input first name')

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print('Input last name')

    def input_postal_code(self, postal_code):
        self.get_postal_code().send_keys(postal_code)
        print('Input postal code')


    def click_continue_button(self):
        self.get_continue_button().click()
        print('Click continue button')

    def save_cart_name_product_1(self):
        cart_name_product_1_text = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_name_product_1)))
        global value_cart_name_product_1_text
        value_cart_name_product_1_text = cart_name_product_1_text.text
        return value_cart_name_product_1_text

    def print_cart_value_name(self):
        print(value_cart_name_product_1_text)

    # Methods

    def input_information(self):
        self.get_current_url()
        self.input_first_name("Donald")
        self.input_last_name("Trump")
        self.input_postal_code("453300")
        self.click_continue_button()
        # self.save_cart_name_product_1()
        # self.print_cart_value_name()
        # self.assert_name_product(Main_page.value_name_product_1_text, value_cart_name_product_1_text)
        # self.assert_word(Main_page.get_name_product_1(), value_cart_name_product_1_text)





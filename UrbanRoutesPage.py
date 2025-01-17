from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import data

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    order_taxi_button = (By.XPATH, '//*[contains(text(), "Pedir un taxi")]')
    comfort_tariff_button = (By.CLASS_NAME, 'tcard')
    telephone_number = (By.CLASS_NAME, "np-button")
    phone_input = (By.ID, 'phone')
    next_button = (By.XPATH, '//*[contains(text(), "Siguiente")]')
    code_field = (By.ID, 'code')
    code_confirmation_button = (By.XPATH, '//*[contains(text(), "Confirmar")]')
    payment_method = (By.CLASS_NAME, "pp-button")
    add_card = (By.XPATH, '//*[contains(text(), "Agregar tarjeta")]')
    card_added = (By.CLASS_NAME, 'pp-row')
    card_number_field = (By.NAME,'number')
    card_code_field = (By.NAME, 'code')
    add_button = (By.XPATH, '//button[text()="Agregar"]')
    card_close_button = (By.CSS_SELECTOR, '.payment-picker.open .modal .section.active .close-button')
    message = (By.ID, 'comment')
    blanket_and_scarves_switch = (By.CLASS_NAME, "switch")
    add_icecream = (By.CLASS_NAME, "counter-plus")
    order_a_taxi = (By.CLASS_NAME, "smart-button-wrapper")
    modal_opcional = (By.XPATH,'//*[contains(text(), "El conductor llegará en")]')
    switch_checkbox = (By.CLASS_NAME, "switch-input")
    icecream_counter = (By.CLASS_NAME, "counter-value")

    def __init__(self, driver):
        self.driver = driver

    # Métodos de acciones en la página
    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def click_order_taxi_button(self):
        self.driver.find_element(*self.order_taxi_button).click()

    def click_comfort_tariff_button(self):
        tariff = self.driver.find_elements(*self.comfort_tariff_button)
        tariff[4].click()


    def click_phone_number_field(self):
        self.driver.find_element(*self.telephone_number).click()

    def fill_in_phone_number(self):
        self.driver.find_element(*self.phone_input).send_keys(data.phone_number)

    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    def set_confirmation_code(self, code):
        self.driver.find_element(*self.code_field).send_keys(code)

    def click_code_confirmation_button(self):
        self.driver.find_element(*self.code_confirmation_button).click()

    def click_payment_method_field(self):
        self.driver.find_element(*self.payment_method).click()

    def click_add_card_button(self):
        self.driver.find_element(*self.add_card).click()

    def enter_card_number(self):
        self.driver.find_element(*self.card_number_field).send_keys(data.card_number)

    def enter_card_code(self):
        self.driver.find_element(*self.card_code_field).send_keys(data.card_code)

    def press_tab_key(self):
        self.driver.find_element(*self.card_code_field).send_keys(Keys.TAB)

    def click_add_button(self):
        add = self.driver.find_element(*self.add_button).click()
        print(add)
    def click_card_close_button(self):
        self.driver.find_element(*self.card_close_button).click()

    def enter_new_message(self):
        self.driver.find_element(*self.message).send_keys(data.message_for_driver)

    def click_blanket_and_scarves_switch(self):
        self.driver.find_element(*self.blanket_and_scarves_switch).click()

    def click_add_icecream(self):
        self.driver.find_element(*self.add_icecream).click()

    def click_order_a_taxi(self):
        self.driver.find_element(*self.order_a_taxi).click()

    def wait_opcional_modal(self):
        self.driver.find_element(*self.modal_opcional)
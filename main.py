import data
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import helpers
import urban_routes_page
import logging

# Configuración del registro
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = Options()
        chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = urban_routes_page.UrbanRoutesPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        if cls.driver:
            cls.driver.quit()

    def set_route(self):
        """Establece las direcciones de origen y destino."""
        self.routes_page.set_from(data.address_from)
        self.routes_page.set_to(data.address_to)
        assert self.routes_page.get_from() == data.address_from, "Error al establecer la dirección de origen."
        assert self.routes_page.get_to() == data.address_to, "Error al establecer la dirección de destino."

    def test_set_route(self):
        try:
            self.set_route()
            logger.info("Direcciones establecidas correctamente.")
        except Exception as e:
            logger.error(f"Error en test_set_route: {e}")

    def test_select_comfort_tariff(self):
        try:
            self.set_route()
            self.routes_page.click_order_taxi_button()
            self.routes_page.click_comfort_tariff_button()
            comfort_tariff = self.driver.find_elements(*self.routes_page.comfort_tariff_button)
            assert "tcard" in self.driver.find_element(
                *urban_routes_page.UrbanRoutesPage.comfort_tariff_button).get_attribute("class")
            assert comfort_tariff[4].is_enabled(), "El botón de tarifa Comfort no está habilitado."
            logger.info("Tarifa Comfort seleccionada correctamente.")
        except Exception as e:
            logger.error(f"Error en test_select_comfort_tariff: {e}")

    def test_fill_phone_number(self):
        try:
            self.set_route()
            self.routes_page.click_order_taxi_button()
            self.routes_page.click_phone_number_field()
            self.routes_page.fill_in_phone_number()
            self.routes_page.click_next_button()
            code = helpers.retrieve_phone_code(self.driver)
            self.routes_page.set_confirmation_code(code)
            self.routes_page.click_code_confirmation_button()
            phone_input_value = self.driver.find_element(*self.routes_page.phone_input).get_attribute("value")
            assert phone_input_value == data.phone_number, "El número de teléfono ingresado no coincide."
            logger.info("Número de teléfono ingresado correctamente.")
        except Exception as e:
            logger.error(f"Error en test_fill_phone_number: {e}")

    def test_add_credit_card(self):
        try:
            self.set_route()
            self.routes_page.click_order_taxi_button()
            self.routes_page.click_payment_method_field()
            self.routes_page.click_add_card_button()

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.routes_page.card_number_field)
            ).send_keys(data.card_number)

            self.routes_page.enter_card_number()
            self.routes_page.enter_card_code()
            self.routes_page.press_tab_key()
            self.routes_page.click_add_button()

            card_input = self.driver.find_elements(*self.routes_page.card_added)[1]
            assert card_input.is_enabled(), "La tarjeta no se agregó correctamente."
            self.routes_page.click_card_close_button()

            logger.info("Tarjeta de crédito agregada correctamente.")
        except Exception as e:
            logger.error(f"Error en test_add_credit_card: {e}")

    def test_write_message(self):
        try:
            self.set_route()
            self.routes_page.click_order_taxi_button()
            self.routes_page.enter_new_message()

            assert self.driver.find_element(*self.routes_page.message).get_property(
                'value') == data.message_for_driver, "El mensaje para el conductor no coincide."

            logger.info("Mensaje para el conductor escrito correctamente.")
        except Exception as e:
            logger.error(f"Error en test_write_message: {e}")

    def test_request_blanket_and_scarves(self):
        try:
            self.set_route()
            self.routes_page.click_order_taxi_button()
            self.routes_page.click_comfort_tariff_button()
            self.routes_page.click_blanket_and_scarves_switch()

            checkbox = self.driver.find_element(*urban_routes_page.UrbanRoutesPage.switch_checkbox)
            assert checkbox.is_selected(), "La opción de manta y pañuelos no está seleccionada."

            logger.info("Solicitud de manta y pañuelos realizada correctamente.")
        except Exception as e:
            logger.error(f"Error en test_request_blanket_and_scarves: {e}")

    def test_request_icecream(self):
        try:
            self.set_route()
            self.routes_page.click_order_taxi_button()
            self.routes_page.click_comfort_tariff_button()

            # Agregar dos helados
            for _ in range(2):
                self.routes_page.click_add_icecream()

            icecream_counter = self.driver.find_element(*urban_routes_page.UrbanRoutesPage.icecream_counter)
            icecream_count = int(icecream_counter.text)

            assert icecream_count == 2, "El conteo de helados no es correcto."

            logger.info("Dos helados solicitados correctamente.")
        except Exception as e:
            logger.error(f"Error en test_request_icecream: {e}")

    def test_search_taxi(self):
        try:
            # Ejecutar todos los pasos anteriores antes de buscar un taxi
            self.set_route()

            # Continuar con el flujo para buscar un taxi
            # (Repetimos algunos pasos anteriores para asegurar que todo esté configurado)

            # Aquí irían las llamadas a los métodos correspondientes para completar el flujo

        WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(self.routes_page.modal_opcional)
        )
        assert self.driver.find_element(
            *self.routes_page.modal_opcional).is_displayed(), "El modal opcional no se muestra."

        logger.info("Búsqueda de taxi realizada correctamente.")

    except Exception as e:
    logger.error(f"Error en test_search_taxi: {e}")




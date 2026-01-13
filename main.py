from data import URBAN_ROUTES_URL, PHONE_NUMBER, ADDRESS_FROM, ADDRESS_TO, MESSAGE_FOR_DRIVER
from helpers import is_url_reachable
from selenium import webdriver
import time
from Urban_Routes_Main_Page import UrbanRoutesMainPage

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(2)
        
        if is_url_reachable(URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

        def teardown_method(self):

            print("teardown method called")
            self.driver.delete_all_cookies()
            self.driver.refresh()
            time.sleep(1)


    def test_set_route(self):
        self.driver.get(URBAN_ROUTES_URL)
        urban_routes_main_page= UrbanRoutesMainPage(self.driver)
        urban_routes_main_page.enter_locations(ADDRESS_FROM,ADDRESS_TO)
        check_from,check_to =urban_routes_main_page.check_addresses()
        assert check_from == ADDRESS_FROM,f'Expected {ADDRESS_FROM} but got {check_from}'
        assert check_to == ADDRESS_TO, f'Expected {ADDRESS_TO} but got {check_to}'
        print("function created for set route")

    def test_select_plan(self):
        self.driver.get(URBAN_ROUTES_URL)
        urban_routes_main_page= UrbanRoutesMainPage(self.driver)
        urban_routes_main_page.enter_locations(ADDRESS_FROM,ADDRESS_TO)
        urban_routes_main_page.click_call_taxi_button()
        urban_routes_main_page.click_selected_supportive()
        actual_value=urban_routes_main_page.check_supportive()
        expected_value="Supportive"
        assert expected_value in actual_value,f'Expected {expected_value} but got {actual_value}'
        print("function created for select plan")

    def test_fill_phone_number(self):
        self.driver.get(URBAN_ROUTES_URL)
        urban_routes_main_page= UrbanRoutesMainPage(self.driver)
        urban_routes_main_page.enter_locations(ADDRESS_FROM,ADDRESS_TO)
        urban_routes_main_page.click_call_taxi_button()
        urban_routes_main_page.click_selected_supportive()
        urban_routes_main_page.enter_taxi_phone()
        actual_value=urban_routes_main_page.get_phone_check()
        expected_value=PHONE_NUMBER
        assert expected_value in actual_value,f'Expected {expected_value} but got {actual_value}'
        print("function created for fill phone number")

    def test_fill_card(self):
        self.driver.get(URBAN_ROUTES_URL)
        urban_routes_main_page= UrbanRoutesMainPage(self.driver)
        urban_routes_main_page.enter_locations(ADDRESS_FROM,ADDRESS_TO)
        urban_routes_main_page.click_call_taxi_button()
        urban_routes_main_page.click_selected_supportive()
        urban_routes_main_page.add_card_number()
        urban_routes_main_page.close_popup()
        actual_value=urban_routes_main_page.check_card_accepted()
        expected_value="Card"
        assert expected_value in actual_value,f'Expected {expected_value} but got {actual_value}'
        print("function created for fill card")

    def test_comment_for_driver(self):
        self.driver.get(URBAN_ROUTES_URL)
        urban_routes_main_page = UrbanRoutesMainPage(self.driver)
        urban_routes_main_page.enter_locations(ADDRESS_FROM, ADDRESS_TO)
        urban_routes_main_page.click_call_taxi_button()
        urban_routes_main_page.click_selected_supportive()
        urban_routes_main_page.message_for_driver()
        actual_value=urban_routes_main_page.check_message()
        expected_value=urban_routes_main_page.check_message()
        assert expected_value in actual_value,f'Expected {expected_value} but got {actual_value}'
        print("function created for comment for driver")


    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(URBAN_ROUTES_URL)
        urban_routes_main_page = UrbanRoutesMainPage(self.driver)
        urban_routes_main_page.enter_locations(ADDRESS_FROM, ADDRESS_TO)
        urban_routes_main_page.click_call_taxi_button()
        urban_routes_main_page.click_selected_supportive()
        urban_routes_main_page.toggle_switch()
        actual_value=urban_routes_main_page.check_blanket_toggle()
        expected_value="true"
        assert expected_value == actual_value,f'Expected {expected_value} but got {actual_value}'
        print("function created for order blanket and handkerchiefs")

    def test_order_2_ice_creams(self):
        self.driver.get(URBAN_ROUTES_URL)
        urban_routes_main_page = UrbanRoutesMainPage(self.driver)
        urban_routes_main_page.enter_locations(ADDRESS_FROM, ADDRESS_TO)
        urban_routes_main_page.click_call_taxi_button()
        urban_routes_main_page.click_selected_supportive()
        urban_routes_main_page.test_order_2_ice_creams()
        actual_value=urban_routes_main_page.check_order_2_ice_creams()
        expected_value="2"
        assert expected_value == actual_value,f'Expected {expected_value} but got {actual_value}'
        print("function created for order 2 ice creams")

    def test_car_search_model_appears(self):
        self.driver.get(URBAN_ROUTES_URL)
        urban_routes_main_page = UrbanRoutesMainPage(self.driver)
        urban_routes_main_page.enter_locations(ADDRESS_FROM, ADDRESS_TO)
        urban_routes_main_page.click_call_taxi_button()
        urban_routes_main_page.click_selected_supportive()
        urban_routes_main_page.enter_taxi_phone()
        urban_routes_main_page.message_for_driver()
        urban_routes_main_page.order_taxi()
        car_search_modal = urban_routes_main_page.driver.find_element(*urban_routes_main_page.ORDER_CAR_SEARCH_LOCATOR)
        assert car_search_modal.is_displayed(), "Car search modal should be visible"
        print("function created for car search model appears")

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
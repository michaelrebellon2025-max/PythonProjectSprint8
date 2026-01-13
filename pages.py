from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import helpers
import time
from selenium.webdriver.common.by import By
from data import PHONE_NUMBER, CARD_NUMBER, CARD_CODE, MESSAGE_FOR_DRIVER


class UrbanRoutesMainPage:
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CUSTOM_OPTION_LOCATOR = (By.XPATH, '//div[text()="Custom"]')
    SCOOTER_ICON_LOCATOR = (By.XPATH, '//img[@src="/static/media/scooter.cf9bb57e.svg"]')
    SCOOTER_TEXT_LOCATOR = (By.XPATH, '//div[@class="results-text"]//div[@class="text"]')
    CAR_ICON_LOCATOR = (By.XPATH, '//img[@src="/static/media/car.8a2b1ff5.svg"]')
    CAR_TEXT_LOCATOR = (By.XPATH, '//div[@class="results-text"]//div[@class="text"]')
    BIKE_ICON_LOCATOR = (By.XPATH, '//img[@src="/static/media/bike.fb41c762.svg"]')
    BIKE_TEXT_LOCATOR = (By.XPATH, '//div[@class="results-text"]//div[@class="text"]')
    CUSTOM_CAR_ICON= (By.XPATH, '//div[@class="type drive"]')
    CLICK_BOOK_LOCATOR = (By.XPATH, '//button[text()="Book"]')
    CAMPING_ICON_LOCATOR= (By.XPATH, '//img[@src="/static/media/camping.075c6361.svg"]')
    CAMPING_TEXT_LOCATOR = (By.XPATH, '//div[@class="drive-preview"]')
    DRIVERS_LICENSE_LOCATOR= (By.XPATH, '//div[@class="np-text"]')
    FIRST_NAME_LOCATOR = (By.XPATH, '//input[@id="firstName"]')
    LAST_NAME_LOCATOR =  (By.XPATH, '//input[@id="lastName"]')
    BIRTHDATE_LOCATOR = (By.XPATH, '//input[@id="birthDate"]')
    CARD_NUMBER_LOCATOR = (By.XPATH, '//input[@id="number"]')
    ADD_CARD_LOCATOR = (By.XPATH, '//input[@id="number"]')
    ADD_CARD_TEXT_LOCATOR = (By.XPATH, '//div[@class="section active"]//div[@style="margin-bottom: 30px;"]')
    DURATION_LOCATOR = (By.XPATH, '//div[@class="duration"]')
    ADD_A_DRIVER_LICENCE_TITLE_LOCATOR = (By.XPATH, '//div[contains(text(),"Add a driver")]')
    SCOOTER_DURATION_LOCATOR= (By.XPATH, '//div[@class="duration"]')
    SUPPORTIVE_ICON_LOCATOR= (By.XPATH, '//img[@src="/static/media/kids.27f92282.svg"]')
    ACTIVE_TARIFF_CARD_LOCATOR = (By.XPATH,'//div[contains(@class,"tcard") and contains(@class,"active")]')
    CALL_A_TAXI_BUTTON_LOCATOR = (By.XPATH, '//button[contains(text(), "Call a taxi")]')
    TAXI_PHONE_LOCATOR = (By.XPATH, '//div[@class="np-text"]')
    TAXI_PHONE_2_LOCATOR = (By.XPATH, '//input[@id="phone"]')
    TAXI_NEXT_BUTTON_LOCATOR = (By.XPATH, '//button[@type="submit"]')
    CODE_TAXI_BUTTON_LOCATOR = (By.ID,"code")
    CODE_SUBMIT_BUTTON_LOCATOR = (By.XPATH, '//button[contains(text(), "Confirm")]')
    CONFIRM_PHONE_NUMBER_LOCATOR = (By.XPATH, '//div[contains(@class,"np-text")]')
    CLICK_CASH_BUTTON_LOCATOR = (By.XPATH, '//img[@src="/static/media/cash.632a51f2.svg"]')
    CLICK_ADD_CARD_LOCATOR = (By.XPATH, '//img[@src="/static/media/plus.d25b8941.svg"]')
    ADD_CARD_NUMBER_LOCATOR = (By.XPATH, '//input[@id="number"]')
    ADD_CARD_CODE_LOCATOR = (By.XPATH, '//input[@name="code"]')
    CLICK_HEADER_LOCATOR = (By.XPATH, '//div[@class="head"][text()="Adding a card"]')
    CLICK_LINK_CARD_LOCATOR = (By.XPATH, '//button[text()="Link"]')
    CLOSE_POPUP_BUTTON = (By.XPATH, '//div[text()= "Payment method"]/preceding-sibling::button[@class="close-button section-close"]')
    CLICK_PAYMENT_LOCATOR = (By.XPATH, '//div[@class="pp-text"]')
    CONFIRM_CARD_ADDED_LOCATOR = (By.XPATH,'//div[@class="pp-value-text"]')
    MESSAGE_FOR_DRIVER_LOCATOR= (By.XPATH, '//input[@id="comment"]')
    BLANKET_TOGGLE_SWITCH_LOCATOR= (By.XPATH, '//input[@class="switch-input"]')
    ICE_CREAM_PLUS_LOCATOR = (By.XPATH, '//div[contains(@class,"counter-plus")][1]')
    ICE_CREAM_COUNT_LOCATOR = (By.XPATH, '//div[@class="counter-value"]')
    CLICK_ORDER_BUTTON_LOCATOR = (By.XPATH, '//span[text()="Order"]')
    ORDER_CAR_SEARCH_LOCATOR = (By.XPATH, '//div[@class="order-header-title"]')



    def __init__(self, driver):
        self.driver = driver
    def enter_locations(self, from_text, to_text):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)
#CHECK ADDRESS
    def check_addresses(self):
        from_address = self.driver.find_element(*self.FROM_LOCATOR).get_attribute('value')
        to_address = self.driver.find_element(*self.TO_LOCATOR).get_attribute('value')
        return from_address, to_address
    def enter_from_location(self,from_text):
        #enters the from field
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)
    def enter_to_location(self,to_text):
        #enters the to field
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)
    def click_custom_option(self):
        #click custom locator
        self.driver.find_element(*self.CUSTOM_OPTION_LOCATOR).click()
    def click_scooter_icon(self):
        # Click Scooter Icon
        self.driver.find_element(*self.SCOOTER_ICON_LOCATOR).click()

    def get_scooter_text(self):
        # Return the "Scooter" text
        return self.driver.find_element(*self.SCOOTER_TEXT_LOCATOR).text

    def click_call_taxi_button(self):
        self.driver.find_element(*self.CALL_A_TAXI_BUTTON_LOCATOR).click()

## CUSTOM FASTEST CAR OPTION

    def click_car_icon(self):
        self.driver.find_element(*self.CAR_ICON_LOCATOR).click()
    def get_car_text(self):
        return self.driver.find_element(*self.CAR_TEXT_LOCATOR).text

##custom bike option
    def click_bike_icon(self):
        self.driver.find_element(*self.BIKE_ICON_LOCATOR).click()
    def get_bike_text(self):
        return self.driver.find_element(*self.BIKE_TEXT_LOCATOR).text

##custom car brand name
    def click_custom_car_icon(self):
        self.driver.find_element(*self.CUSTOM_CAR_ICON).click()
    def click_book(self):
        self.driver.find_element(*self.CLICK_BOOK_LOCATOR).click()
    def click_camping(self):
        self.driver.find_element(*self.CAMPING_ICON_LOCATOR).click()
    def get_camping_text(self):
        return self.driver.find_element(*self.CAMPING_TEXT_LOCATOR).text


#ADD CARD- FIRST-LAST-BIRTH-AND CARD#
    def enter_card_information(self,first_name,last_name,birth_date,card_number):
        self.driver.find_element(*self.FIRST_NAME_LOCATOR).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_LOCATOR).send_keys(last_name)
        self.driver.find_element(*self.BIRTHDATE_LOCATOR).send_keys(birth_date)
        self.driver.find_element(*self.CARD_NUMBER_LOCATOR).send_keys(card_number)
        self.driver.find_element(*self.ADD_A_DRIVER_LICENCE_TITLE_LOCATOR).click()
        self.driver.find_element(*self.ADD_CARD_LOCATOR).click()


    def click_drivers_license_icon(self):
        self.driver.find_element(*self.DRIVERS_LICENSE_LOCATOR).click()
    def enter_first_name(self,first_name):
        self.driver.find_element(*self.FIRST_NAME_LOCATOR).send_keys(first_name)
    def enter_last_name(self,last_name):
        self.driver.find_element(*self.LAST_NAME_LOCATOR).send_keys(last_name)
    def enter_birth_date(self,birth_date):
        self.driver.find_element(*self.BIRTHDATE_LOCATOR).send_keys(birth_date)
    def enter_card_number(self,card_number):
        self.driver.find_element(*self.CARD_NUMBER_LOCATOR).send_keys(card_number)
    def click_add_card(self):
        self.driver.find_element(*self.ADD_CARD_LOCATOR).click()
    def get_add_card_text(self):
        return self.driver.find_element(*self.ADD_CARD_TEXT_LOCATOR).text
#DURATION test
    def get_duration_text(self):
        return self.driver.find_element(*self.DURATION_LOCATOR).text
    def get_scooter_duration_text(self):
        return self.driver.find_element(*self.SCOOTER_DURATION_LOCATOR).text
#ADD PHONE
    def enter_taxi_phone(self):
        self.driver.find_element(*self.TAXI_PHONE_LOCATOR).click()
        self.driver.find_element(*self.TAXI_PHONE_2_LOCATOR).send_keys(PHONE_NUMBER)
        self.driver.find_element(*self.TAXI_NEXT_BUTTON_LOCATOR).click()
        code=helpers.retrieve_phone_code(self.driver)
        self.driver.find_element(*self.CODE_TAXI_BUTTON_LOCATOR).send_keys(code)
        self.driver.find_element(*self.CODE_SUBMIT_BUTTON_LOCATOR).click()
    def get_phone_check(self):
        return self.driver.find_element(*self.CONFIRM_PHONE_NUMBER_LOCATOR).text
#ADD CARD
    def add_card_number(self):
        wait = WebDriverWait(self.driver, 10)

        # Open payment section
        self.driver.find_element(*self.CLICK_PAYMENT_LOCATOR).click()
        self.driver.find_element(*self.CLICK_ADD_CARD_LOCATOR).click()

        card_input = wait.until(EC.visibility_of_element_located(self.ADD_CARD_NUMBER_LOCATOR))
        card_input.clear()
        card_input.send_keys(CARD_NUMBER)

        code_input = wait.until(EC.visibility_of_element_located(self.ADD_CARD_CODE_LOCATOR))
        code_input.clear()
        code_input.send_keys(CARD_CODE)

        # Remove focus
        self.driver.find_element(*self.CLICK_HEADER_LOCATOR).click()
        #self.driver.find_element(*self.CLICK_LINK_CARD_LOCATOR).click()
        # Link card
        wait.until(EC.element_to_be_clickable(self.CLICK_LINK_CARD_LOCATOR)).click()

    def close_popup(self):
        self.driver.find_element(*self.CLOSE_POPUP_BUTTON).click()

    def check_card_accepted(self):
        return self.driver.find_element(*self.CONFIRM_CARD_ADDED_LOCATOR).text

#MESSAGE FOR DRIVER
    def message_for_driver(self):
        self.driver.find_element(*self.MESSAGE_FOR_DRIVER_LOCATOR).send_keys(MESSAGE_FOR_DRIVER)
    def check_message(self):
        return self.driver.find_element(*self.MESSAGE_FOR_DRIVER_LOCATOR).text

#TOGGLE BLANKET SWITCH
    def toggle_switch(self):
        toggle = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.BLANKET_TOGGLE_SWITCH_LOCATOR)
        )

        if not toggle.is_selected():
            self.driver.execute_script("arguments[0].click();", toggle)
            print("✅ Toggle switch activated.")
        else:
            print("ℹ️ Toggle already active.")
    def check_blanket_toggle(self):
        return self.driver.find_element(*self.BLANKET_TOGGLE_SWITCH_LOCATOR).get_attribute("checked")

    def click_selected_supportive(self):
        element = self.driver.find_element(By.XPATH, '//img[@src="/static/media/kids.27f92282.svg"]')
        css = element.get_attribute("class")

        if "active" in css:
            pass  # Already selected, no action needed
        else:
            element.click()  # Click to select it

    def check_supportive(self):
        active_card = self.driver.find_element(*self.ACTIVE_TARIFF_CARD_LOCATOR)
        return active_card.find_element(By.CLASS_NAME, "tcard-title").text
    def test_order_2_ice_creams(self):
        desired_amount = 2
        #Get current count
        current_count = int(
            self.driver.find_element(*self.ICE_CREAM_COUNT_LOCATOR).text)
        print(f"Current ice creams in order: {current_count}")
        if current_count < desired_amount:
            for i in range(desired_amount - current_count):
                print(f"Adding ice cream #{current_count + i + 1}")
                self.driver.find_element(*self.ICE_CREAM_PLUS_LOCATOR).click()
    def check_order_2_ice_creams(self):
        return self.driver.find_element(*self.ICE_CREAM_COUNT_LOCATOR).text

#order supportive taxi
    def order_taxi(self):
        self.driver.find_element(*self.CLICK_ORDER_BUTTON_LOCATOR).click()
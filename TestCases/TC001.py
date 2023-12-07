import time
import unittest
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# Excepciones directo del selenium
from selenium.common.exceptions import TimeoutException
# acciones del teclado, mouse y perifericos
from selenium.webdriver.common.action_chains import ActionChains

from Locators.Locators import MyLocators


class TC001():

    def __init__(self, driver):
        self.driver = driver
        self.name_user_name = MyLocators.name_user_name
        self.name_user_password = MyLocators.name_user_password
        self.root_csv = pd.read_csv(MyLocators.root_csv)

        self.add_to_cart_items = MyLocators.add_to_cart_items
        self.class_shopping_cart_link = MyLocators.class_shopping_cart_link
        self.remove_cart_button = MyLocators.remove_cart_button
        self.name_checkout_button = MyLocators.name_checkout_button

        self.cart_item_element = MyLocators.cart_item_element
        self.name_first_name = MyLocators.name_first_name
        self.name_last_name = MyLocators.name_last_name
        self.name_postal_code = MyLocators.name_postal_code
        self.name_continue_button = MyLocators.name_continue_button

        self.xpath_payment_information = MyLocators.xpath_payment_information
        self.xpath_shipping_information = MyLocators.xpath_shipping_information
        self.xpath_price_total_information = MyLocators.xpath_price_total_information
        self.name_finish_button = MyLocators.name_finish_button
        self.id_burger_menu_button = MyLocators.id_burger_menu_button
        self.class_name_complete_header = MyLocators.class_name_complete_header
        self.id_logout_sidebar_link = MyLocators.id_logout_sidebar_link

    def start(self):
        global i
        global df

        for i in range(len(self.root_csv)):
            #print(self.root_csv.iloc[i]["Y/N"])
            if self.root_csv.iloc[i]["Y/N"] == "Y":

                method_name = self.root_csv.iloc[i]["Nombre"]
                try:
                    test_method = getattr(TC001, method_name)
                    test_method(self)

                except AttributeError as e:
                    print("Error!")
                    print(e)
            else:
                pass

    def Test_001(self):
        print(f"Test Sequence: {self.root_csv.iloc[i]['ID Test']}")

        self.driver.get(MyLocators.URL)
        # self.driver.maximize_window()
        self.driver.implicitly_wait(2)

        # Login Session
        print("Login")
        user_from_csv = self.root_csv.iloc[i]["Username"]
        password_from_csv = self.root_csv.iloc[i]["Password"]
        self.driver.find_element(
            By.NAME, self.name_user_name).send_keys(user_from_csv)
        self.driver.find_element(
            By.NAME, self.name_user_password).send_keys(password_from_csv)
        self.driver.find_element(
            By.NAME, self.name_user_password).send_keys(Keys.ENTER)

        time.sleep(1)

        # Add 6 items to cart
        key = self.root_csv.iloc[i]["Item1"].lower()
        self.driver.find_element(By.NAME, self.add_to_cart_items[key]).click()
        time.sleep(1)
        
        key = self.root_csv.iloc[i]["Item2"].lower()
        self.driver.find_element(By.NAME, self.add_to_cart_items[key]).click()
        time.sleep(1)
        
        key = self.root_csv.iloc[i]["Item3"].lower()
        self.driver.find_element(By.NAME, self.add_to_cart_items[key]).click()
        time.sleep(1)
        
        key = self.root_csv.iloc[i]["Item4"].lower()
        self.driver.find_element(By.NAME, self.add_to_cart_items[key]).click()
        time.sleep(1)
        
        key = self.root_csv.iloc[i]["Item5"].lower()
        self.driver.find_element(By.NAME, self.add_to_cart_items[key]).click()
        time.sleep(1)
        
        key = self.root_csv.iloc[i]["Item6"].lower()
        self.driver.find_element(By.NAME, self.add_to_cart_items[key]).click()
        time.sleep(1)

        # Click to cart
        item = self.driver.find_element(
            By.CLASS_NAME, self.class_shopping_cart_link)
        item.click()
        time.sleep(1)
        
        # Remove second item
        elements = self.driver.find_elements(
            By.CLASS_NAME, self.cart_item_element)
        
        #Only deletes the second item if a list has two or more items
        index_to_remove = self.root_csv.iloc[i]["Remove_index"]
        if len(elements) >= index_to_remove:
            index_to_remove = int(index_to_remove) - 1
            print(elements[index_to_remove])
            elements[index_to_remove].find_element(By.CLASS_NAME, "cart_button").click()
        else:
            print("There are not second item.")

        time.sleep(1)
        
        # Checkout cart
        self.driver.find_element(By.NAME, self.name_checkout_button).click()
        time.sleep(1)

        # Filling Checkout information
        self.driver.find_element(By.NAME, self.name_first_name).send_keys(
            self.root_csv.iloc[i]["First_Name"])
        self.driver.find_element(By.NAME, self.name_last_name).send_keys(
            self.root_csv.iloc[i]["Last_Name"])
        self.driver.find_element(By.NAME, self.name_postal_code).send_keys(
           str(self.root_csv.iloc[i]["Postal_Code"]))
        time.sleep(1)

        # Click on Continue button
        self.driver.find_element(By.NAME, self.name_continue_button).click()
        time.sleep(1)

        # Checkout information
        try:
            message = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH,
                                                  self.xpath_payment_information))
            )
            print("Message Payment: ", str(message.text))

            # df.loc[current_row, 'Mensaje'] = message.text
            message = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH,
                                                  self.xpath_shipping_information))
            )
            print("Message Shipping: ", str(message.text))

            message = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH,
                                                  self.xpath_price_total_information))
            )
            print("Message Price: ", str(message.text))

        except TimeoutException as toe:
            print("Can't find any element: ", toe)
            return

        time.sleep(1)

        # Click to Finish Button
        self.driver.find_element(By.NAME, self.name_finish_button).click()
        time.sleep(1)

        # Wait for Thanks screen
        try:
            message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME,
                                                  self.class_name_complete_header))
            )
            print("Message Thanks: ", str(message.text))

        except TimeoutException as toe:
            print("Can't find Thanks element: ", toe)
            return

        # Click on menu
        self.driver.find_element(By.ID, self.id_burger_menu_button).click()
        time.sleep(1)

        # Click on Log out
        self.driver.find_element(By.ID, self.id_logout_sidebar_link).click()
        time.sleep(4)

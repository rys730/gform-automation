import random
from typing import Optional
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver

def init_firefox_driver(
    options: Optional[webdriver.FirefoxOptions]=None
) -> webdriver.Firefox:
    driver = webdriver.Firefox(options=options)
    return driver

class GformDriver:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
    
    def set_gform_url(self, url: str):
        self.url = url
    
    def radio_question(self, params):
        form = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//div[contains(@data-params, '{params}')]"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", form)
        radio_buttons = form.find_elements(by=By.XPATH, value=".//div[@role='radio']")
        selected_gender = random.choice(radio_buttons)
        selected_gender.click()
        return

    def radio_question_fixed_answer(self, params: str, answer_index: int):
        form = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//div[contains(@data-params, '{params}')]"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", form)
        buttons = WebDriverWait(form, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, ".//div[@role='radio']"))  # Adjust the XPath as necessary
        )

        button_to_click = buttons[answer_index]
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button_to_click)
        button_to_click.click()
        return        

    def text_question(self, params: str, answer: str):
        form = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//div[contains(@data-params, '{params}')]"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", form)
        input_form = form.find_element(by=By.XPATH, value=".//input")
        input_form.click()
        input_form.send_keys(answer)
        return
        
    def next_page_button(self, text: str = "Next"):
        next_button = self.driver.find_element(By.XPATH, f"//span[text()='{text}']/ancestor::div[@role='button']")
        next_button.click()
        return


# this will contain all the methods

import booking.constant as const
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from booking.booking_filter import BookingFiltration

# Booking class is inheriting from webdriver.Chrome
class Booking(webdriver.Chrome):
    def __init__(self,teardown=False):
        options = webdriver.ChromeOptions() 
        options.add_experimental_option("detach", True)  
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.teardown=teardown
        super().__init__(options=options)
        self.implicitly_wait(5)
        self.maximize_window()
        
    def land_first_page(self): 
        self.get(const.BASE_URL)
        
    def handle_popup(self):
        try:
            popup = WebDriverWait(self, 2).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='popup-close']"))
            )
            popup.click()
        except:
            pass 
        
    def change_currency(self,currency):
        currency_elem=WebDriverWait(self,10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,"button[data-testid='header-currency-picker-trigger']")
            )
             )
        currency_elem.click()
        time.sleep(3)
        
        target_Currenc=WebDriverWait(self,10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//div[contains(@class,'CurrencyPicker_currency') and normalize-space(text())='{currency}']")   
            )
        )
        target_Currenc.find_element(By.XPATH, "..").click()
       
        
    def place_to_go(self,place):
        place_to_goo=WebDriverWait(self,10).until(
            EC.element_to_be_clickable(
                (By.NAME,"ss")
            )
        )
        place_to_goo.clear()
        place_to_goo.send_keys(place)
        
       
        target_place = WebDriverWait(self, 10).until(
            EC.element_to_be_clickable(
        (       By.XPATH, f"//li[@role='option']//div[contains(normalize-space(.), '{place}')]")
    )
)
        target_place.click()
        
    def dates(self,checkin,checkout):
        check_in_date=WebDriverWait(self,10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,f'span[data-date="{checkin}"]')
            )
        )
        check_in_date.click()
        check_out_date=WebDriverWait(self,10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,f'span[data-date="{checkout}"]')
            )
        )
        check_out_date.click()
        
    def select_adults(self,count=0):
        adults=WebDriverWait(self,10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,'button[data-testid="occupancy-config"]')
            )
        )
        adults.click()
        while True:
            slider_value=WebDriverWait(self,10).until(
                EC.presence_of_element_located(
                    (By.ID,"group_adults")
                )
            )
            curr_value=slider_value.get_attribute("value")
            if int(curr_value)==1:
                break
            
            dec_adult=WebDriverWait(self,10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR,"button[class*='c857f39cb2']")
                )
            )
            dec_adult.click()
        inc_adult=WebDriverWait(self,10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,"button[class*='dc8366caa6']")
            )
        )
        for _ in range(count-1):
            inc_adult.click()
        
    def clicksearch(self):
        search=WebDriverWait(self,10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,"button[type='submit']")
            )
        )
        search.click()
        
    def apply_filtration(self):
        filtration=BookingFiltration(driver=self)    #self here is Booking object (a Chrome driver)
        filtration.applystar(3)
        filtration.price()
        
        
    def __exit__(self,exc_type,exc_val,exc_tab):
        if self.teardown:
             self.quit()
       
       



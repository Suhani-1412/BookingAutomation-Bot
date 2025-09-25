from selenium.webdriver.remote.webdriver import WebDriver   
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class BookingFiltration:
    def __init__(self,driver:WebDriver):  
        self.driver=driver
    
    def applystar(self, *star_vals):   #* star_vals is for passing multiple values
        for star_val in star_vals:
            star_checkbox_label = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, f"div[data-filters-item='class:class={star_val}'] label")
                )
            )
            star_checkbox_label.click()
            
    def price(self):
        sortbutton=WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,"button[data-testid='sorters-dropdown-trigger']")
            )
        )
        sortbutton.click()
        pricebutton=WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,"button[data-id='price']")
            )
        )
        pricebutton.click()
                

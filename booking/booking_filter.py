from selenium.webdriver.remote.webdriver import WebDriver   #we imported this bcz we were not getting suggestions from driver only bcz our compiler doesnt know that driver is a web driver so thts why
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class BookingFiltration:
    def __init__(self,driver:WebDriver):   #this self is function self ya object self not chrome driver self,for chrome driver we used driver as an argument
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
                


# f"div[data-filters-item='class:class={star_val}'] label")

# On this page, the <input> checkbox is hidden (type="checkbox"), and it is not directly clickable.
# Selenium can only click elements that are visible and interactable.
# he <label> next to the <input> is visible and handles the click for the checkbox automatically.
# Clicking the <label> toggles the checkbox, so it works exactly like a user click.
# We wrap it with EC.element_to_be_clickable → ensures Selenium waits for the label to appear and be interactable
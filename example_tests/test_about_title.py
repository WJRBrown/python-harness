import time
from selenium.webdriver.common.by import By

def Run(Runner):
    Runner.driver.find_element(By.ID, 'about').click()
    title = Runner.driver.title
    time.sleep(1)
    if title == "About Python™ | Python.org":
        return True
    else:
        Runner.set_message("Expected: 'About Python™ | Python.org'\nActual: '%s'" % title)
        return False

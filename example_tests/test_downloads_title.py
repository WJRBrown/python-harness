import time
from selenium.webdriver.common.by import By

def Run(Runner):
    Runner.driver.find_element(By.ID, 'downloads').click()
    title = Runner.driver.title
    time.sleep(1)
    if title == "Download Python | Python.org":
        return True
    else:
        Runner.set_message("Expected: 'Download Python | Python.org'\nActual: '%s'" % title)
        return False

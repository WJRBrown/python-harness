import time
from selenium.webdriver.common.by import By

def Run(Runner):
    Runner.driver.find_element(By.ID, 'documentation').click()
    title = Runner.driver.title
    time.sleep(1)
    if title == "Our Documentation | Python.org":
        return True
    else:
        Runner.set_message("Expected: 'Our Documentation | Python.org'\nActual: '%s'" % title)
        return False

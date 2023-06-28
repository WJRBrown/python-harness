import time
from selenium.webdriver.common.by import By

def Run(Runner):
    Runner.driver.find_element(By.ID, 'news').click()
    title = Runner.driver.title
    time.sleep(1)
    if title == "Our Blogs | Python.org":
        return True
    else:
        Runner.set_message("Expected: 'Welcome to Python.org'\nActual: '%s'" % title)
        return False

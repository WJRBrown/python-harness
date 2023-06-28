import os
import time
from selenium import webdriver

class TestRunner():
    def __init__(self, root_path, target_page):
        self.root = root_path
        self.page = target_page
        self.driver = webdriver.Chrome()
        self.driver.get(self.page)
        self.message = ""
        
    def load_index(self):
        self.driver.get(self.page)
    
    def close_page(self):
        self.driver.close()
        
    def set_message(self, msg):
        self.message = msg

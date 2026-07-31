"""

https://books.toscrape.com/index.html

"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestEses(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        #time.sleep(3)


    def test_eses_content(self):
        self.driver.get("https://eses.name")
        #time.sleep(3)
        self.assertIn("nix", self.driver.page_source)


 
    def test_eses_content_notfound(self):
            self.driver.get("https://eses.name")
            #time.sleep(3)
            self.driver.save_screenshot("screenshot.png")
            self.assertIn("nixx", self.driver.page_source)
    

    
    def tearDown(self):
        self.driver.quit()


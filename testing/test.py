from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from time import sleep
from HTMLTestRunner.runner import HTMLTestRunner
import unittest

class ChatifyUnitTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(service=Service(r"C:\Users\Mashu\Desktop\selenium-testing\chromedriver.exe"))
        self.addCleanup(self.browser.quit)
        
    def test1_homepage(self):
        """Check if homepage is loaded properly."""
        self.browser.get('http://localhost:5000')
        sleep(3)
        element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/div[1]/div[1]/a')
        assert element.text == "Chat-iFy", "Homepage is not loaded properly."
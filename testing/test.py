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

    def test2_navbar_chat(self):
        """Check if Login Page is loaded properly via the Nav-Bar."""
        self.browser.get('http://localhost:5000')
        sleep(3)
        element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/div[1]/div[2]/ul/li[2]/a')
        element.click()
        sleep(3)
        # assert "Login chat-iFy" in self.browser.page_source, "Login Page could not be accessed via the Nav-Bar"
        login_button = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/div[3]/button')
        assert login_button is not None, "Login Page could not be accessed via the Nav-Bar"

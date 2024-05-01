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
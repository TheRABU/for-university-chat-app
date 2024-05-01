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

    def test3_navbar_register(self):
        """Check if Register Page is loaded properly via the Nav-Bar."""
        self.browser.get('http://localhost:5000')
        sleep(3)
        element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div[2]/ul/li[4]/a')
        element.click()
        sleep(3)
        signup_button = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/div[6]/button')
        assert signup_button is not None, "SignUp Page could not be accessed via the Nav-Bar"
        # assert "Sign Up Chat-i-Fy" in self.browser.page_source, "Signup Page could not be accessed via the Nav-Bar"

    def test4_navbar_aboutus(self):
        """Check if Login Page is loaded properly via the Nav-Bar."""
        self.browser.get('http://localhost:5000')
        sleep(3)
        element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/div[1]/div[2]/ul/li[3]/a')
        element.click()
        sleep(3)
        assert "Want to know more about the members?" in self.browser.page_source, "About Us Page could not be accessed via the Nav-Bar"
        
    def test5_signup(self):
        """Check if that signup page is working properly with correct input."""
        self.browser.get("http://localhost:5000/signup")
        name_input_element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/div[1]/input')
        username_input_element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/div[2]/input')
        password1_input_element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/div[3]/input')
        password2_input_element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/div[4]/input')
        check_box = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/div[5]/div[1]/label/input')
        signup_button = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/div[6]/button')

        for char in "testuser":
            name_input_element.send_keys(char)
            sleep(0.2)

        for char in "testuser":
            username_input_element.send_keys(char)
            sleep(0.2)

        for char in "123456":
            password1_input_element.send_keys(char)
            sleep(0.2)
        for char in "123456":
            password2_input_element.send_keys(char)
            sleep(0.2)
        check_box.click()
        sleep(2)
        signup_button.click()
        sleep(1)
        assert "Username already exists" in self.browser.page_source, "Sigup is not working properly"


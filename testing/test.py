from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from time import sleep
from HTMLTestRunner.runner import HTMLTestRunner
import unittest


def generateMessage():
    import datetime
    return "Test Message Generated at " + str(datetime.datetime.now())


class ChatifyUnitTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(service=Service(r".\chromedriver.exe"))
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

    def test6_login(self):
        """Check if that login page is working properly with correct input."""
        self.browser.get("http://localhost:5000/login")
        username_input_element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/div[1]/input')
        password1_input_element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/div[2]/input')
        login_button = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/div[3]/button')
        
        for char in "testuser":
            username_input_element.send_keys(char)
            sleep(0.2)

        for char in "123456":
            password1_input_element.send_keys(char)
            sleep(0.2)
        sleep(2)
        login_button.click()
        sleep(3)

        assert "Select a chat to start messaging" in self.browser.page_source, "Login is not working properly"

    def test7_chat(self):
        """Check if instant messagning is working or not."""
        self.browser.get("http://localhost:5000/login")
        username_input_element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/div[1]/input')
        password1_input_element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/div[2]/input')
        login_button = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/div[3]/button')
        
        for char in "testuser":
            username_input_element.send_keys(char)
            sleep(0.2)

        for char in "123456":
            password1_input_element.send_keys(char)
            sleep(0.2)
        sleep(2)
        login_button.click()
        sleep(3)

        other_user = self.browser.find_element(By.XPATH, f"//*[contains(text(), 'testreg')]")
        other_user.click()
        sleep(5)

        message_input = self.browser.find_element(By.XPATH, f"/html/body/div/div/div[1]/main/div[2]/form/div/input")

        message = generateMessage()
        for char in message:
            message_input.send_keys(char)
            sleep(0.1)
        
        message_send_button = self.browser.find_element(By.XPATH, f"/html/body/div/div/div[1]/main/div[2]/form/div/button")
        sleep(2)
        message_send_button.click()
        sleep(2)
        assert message in self.browser.page_source, "Instant messaging is not working properly."
        sleep(5)

    def test8_logout(self):
        """Check if that logout is working properly."""
        self.browser.get("http://localhost:5000/login")
        username_input_element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/div[1]/input')
        password1_input_element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/div[2]/input')
        login_button = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/div[3]/button')
        
        for char in "testuser":
            username_input_element.send_keys(char)
            sleep(0.2)

        for char in "123456":
            password1_input_element.send_keys(char)
            sleep(0.2)
        sleep(2)
        login_button.click()
        sleep(3)

        assert "Select a chat to start messaging" in self.browser.page_source, "Login is not working properly"

        logout_button = self.browser.find_element(By.CSS_SELECTOR, '.text-black')

        sleep(2)

        logout_button.click()

        sleep(2)
        
        assert self.browser.current_url == "http://localhost:5000/login"
        sleep(1)

        
if __name__ == '__main__':
    # unittest.main(verbosity=2)
    my_test_suite = unittest.TestSuite()
    my_test_suite.addTest(unittest.makeSuite(ChatifyUnitTest))
    runner = HTMLTestRunner(
        title='''Chatify App Test''', open_in_browser=True,
        tested_by="Maisha Zaman")
    runner.run(my_test_suite)
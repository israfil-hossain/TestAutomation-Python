import time 
from selenium import webdriver

baseUrl = 'https://www.flickr.com/'
driverpath = 'J:\Selenium\drivers\chromedriver.exe' 

class SigninClassTest():
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = driverpath)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window() 

    def signin(self):
        self.driver.get(baseUrl) 
        # Click Login Button 
        self.driver.find_element_by_link_text("Log In").click()
        # Fillup Email TextBox 
        self.driver.find_element_by_id("login-email").send_keys("israfilhossain166091@gmail.com")
        # Click Next Button
        self.driver.find_element_by_xpath('//*[@id="login-form"]/button/span').click() 
        # Fillup password TextBox 
        self.driver.find_element_by_id('login-password').send_keys('123456789abc')
        # Click Login Button 
        self.driver.find_element_by_xpath('//*[@id="login-form"]/button').click()
        time.sleep(8) 

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
        
if __name__ == '__main__':
    obj = SigninClassTest()
    obj.setUpClass()
    obj.signin() 
    obj.tearDown() 

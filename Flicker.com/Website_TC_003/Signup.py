import time 
from selenium import webdriver

baseUrl = 'https://www.flickr.com/'
driverpath = 'J:\Selenium\drivers\chromedriver.exe' 

class SignupTestClass():
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = driverpath)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window() 

    def Signup(self):
        self.driver.get(baseUrl) 
        self.driver.find_element_by_link_text("Sign Up").click()
        self.driver.find_element_by_id("sign-up-first-name").send_keys("Israfil") 
        self.driver.find_element_by_id("sign-up-last-name").send_keys("Hossain") 
        self.driver.find_element_by_id("sign-up-age").send_keys("24") 
        self.driver.find_element_by_id("sign-up-email").send_keys("israfilhossain166091@gmail.com") 
        self.driver.find_element_by_id("sign-up-password").send_keys("123456789abc")
        time.sleep(20) 
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[1]/form/button').click() 
        time.sleep(20) 
    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
if __name__ == '__main__':
    obj = SignupTestClass()
    obj.setUpClass()
    obj.Signup() 
    obj.tearDown() 

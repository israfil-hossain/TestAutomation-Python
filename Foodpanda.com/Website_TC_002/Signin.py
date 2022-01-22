import time 
from selenium import webdriver
from selenium.webdriver.common.by import By

baseUrl = 'https://www.foodpanda.com.bd/'
driverpath = 'J:\Selenium\drivers\chromedriver.exe' 

class SigninClassTest():
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = driverpath)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window() 

    def TC_2_1_signin_google(self):
        time.sleep(5)
        self.driver.get(baseUrl) 
        self.driver.implicitly_wait(40)
        time.sleep(50) 
        self.driver.find_element(By.XPATH,'/html/body/div[1]/header/div[3]/div/a').click()
        time.sleep(10) 
    def TC_2_2_signin_facebook(self):
        self.driver.get(baseUrl)
    def TC_2_3_signin_mail(self):
        self.driver.get(baseUrl) 

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
        
if __name__ == '__main__':
    obj = SigninClassTest()
    obj.setUpClass()
    obj.TC_2_1_signin_google() 
    obj.tearDown() 

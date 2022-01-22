import time 
from selenium import webdriver
from selenium.webdriver.common.by import By

baseUrl = 'https://www.rokomari.com/book'
driverpath = 'J:\Selenium\drivers\chromedriver.exe' 

class SigninClassTest():
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = driverpath)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window() 


    def TC_2_1_signin_facebook(self):
        self.driver.get(baseUrl)
        # Remove Pop-up message 
        self.driver.find_element(By.XPATH,'//*[@id="js--entry-popup"]/div[1]/button').click()
        # Click Sign-in button 
        self.driver.find_element_by_link_text("Sign in").click()
        time.sleep(3)
        # Click Facebook button 
        self.driver.find_element_by_xpath('//*[@id="js--login-form"]/div[1]/div/button[1]').click()
        time.sleep(3)
        # Fill-up Email box 
        self.driver.find_element_by_id("email").send_keys("jonyakash45@gmail.com")
        time.sleep(2) 
        # Fill-up Password box 
        self.driver.find_element_by_id("pass").send_keys("11111111")
        time.sleep(3) 
        # Click Loginbutton 
        self.driver.find_element_by_id("loginbutton").click()
        time.sleep(5) 
        # self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div/div/div/div[1]/div/span/span').click()
    
    def TC_2_2_signin_google(self):

        self.driver.get(baseUrl) 
        time.sleep(5) 
        # Click Sign-in button 
        # self.driver.find_element(By.XPATH,'//*[@id="js--entry-popup"]/div[1]/button').click()
        self.driver.find_element_by_link_text("Sign in").click()
        time.sleep(3) 
        self.driver.find_element(By.XPATH,'//*[@id="js--login-form"]/div[1]/div/button[2]').click()
        time.sleep(10) 
    

    def TC_2_3_signin_mail(self):
        self.driver.get(baseUrl)
        # Click Sign-in button 
        self.driver.find_element_by_link_text("Sign in").click()
        time.sleep(5) 
        #Fillup email box 
        self.driver.find_element(By.ID,'j_username').send_keys('obujbalok467@gmail.com')
        time.sleep(2) 
        # Fillup Password box 
        self.driver.find_element(By.NAME,'j_password').send_keys('18378442Jony')
        time.sleep(3) 
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/section/div[2]/div[2]/form/button').click() 
        time.sleep(10) 


    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
        
if __name__ == '__main__':
    obj = SigninClassTest()
    obj.setUpClass()
    obj.TC_2_1_signin_facebook()
    obj.TC_2_2_signin_google() 
    obj.TC_2_3_signin_mail() 
    obj.tearDown() 

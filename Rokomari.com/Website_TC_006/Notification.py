import time 
from selenium import webdriver
from selenium.webdriver.common.by import By

baseUrl = 'https://www.rokomari.com/book'
driverpath = 'J:\Selenium\drivers\chromedriver.exe' 

class NotificationClassTest():
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = driverpath)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window() 

    def signin(self):
        self.driver.get(baseUrl)
        # Click Sign-in button 
        self.driver.find_element(By.LINK_TEXT,"Sign in").click()
        time.sleep(5) 
        #Fillup email box 
        self.driver.find_element(By.ID,'j_username').send_keys('obujbalok467@gmail.com')
        time.sleep(2) 
        # Fillup Password box 
        self.driver.find_element(By.NAME,'j_password').send_keys('18378442Jony')
        time.sleep(3) 
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/section/div[2]/div[2]/form/button').click() 
        time.sleep(5)
        # Remove Pop-up message 
        self.driver.find_element(By.XPATH,'//*[@id="js--entry-popup"]/div[1]/button').click() 
        time.sleep(5) 
        self.driver.find_element(By.XPATH,'/html/body/header/div/div/div/div/div[3]/div/div[2]/a').click()

    def notification(self):
        self.driver.find_element(By.XPATH,'//*[@id="js-cart-menu"]').click()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT,'View All').click()
        time.sleep(5)

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
        
if __name__ == '__main__':
    obj = NotificationClassTest()
    obj.setUpClass()
    obj.signin()
    obj.notification()
    obj.tearDown() 
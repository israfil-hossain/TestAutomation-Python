import time 
from selenium import webdriver
from selenium.webdriver.common.by import By

baseUrl = 'https://www.rokomari.com/book'
driverpath = 'J:\Selenium\drivers\chromedriver.exe' 

class TopbarClassTest():
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = driverpath)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window() 

    def TC_8_1_book(self):
        self.driver.get(baseUrl)
        # Remove Pop-up message 
        self.driver.find_element(By.XPATH,'//*[@id="js--entry-popup"]/div[1]/button').click() 
        time.sleep(5) 

    def TC_8_2_electronics(self):
        # Click electronics button 
        self.driver.find_element(By.XPATH,'/html/body/header/div/nav/div/div[1]/ul/li[2]/a').click()
        time.sleep(5)
        # self.driver.find_element(By.XPATH,'//*[@id="js--exit-intent"]/div[1]/button').click()
        # time.sleep(3) 
        


    def TC_8_3_stationary(self):
        # Click stationary button 
        self.driver.find_element(By.XPATH,'/html/body/header/div/nav/div/div[1]/ul/li[3]/a').click()
        time.sleep(5)

    def TC_8_4_giftfinder(self):
        # Click giftfinder button 
        self.driver.find_element(By.XPATH,'/html/body/header/div/nav/div/div[1]/ul/li[4]/a').click()
        time.sleep(5)



    def TC_8_5_organization_order(self):
        # Click order button 
        self.driver.find_element(By.XPATH,'/html/body/header/div[6]/div/div/div/ul/li[5]/a').click()
        time.sleep(5)

    def TC_8_6_offer(self):
        # Click Offer button 
        self.driver.find_element(By.XPATH,'/html/body/header/div[6]/div/div/div/ul/li[6]/a').click()
        time.sleep(5)

    def TC_8_7_blog(self):
        # Click blog button 
        self.driver.find_element(By.LINK_TEXT,'ব্লগ').click()
        time.sleep(10)

    
    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

    
if __name__ == '__main__':
    obj = TopbarClassTest()
    obj.setUpClass()
    obj.TC_8_1_book() 
    obj.TC_8_2_electronics() 
    obj.TC_8_3_stationary() 
    obj.TC_8_4_giftfinder() 
    obj.TC_8_5_organization_order() 
    obj.TC_8_6_offer() 
    obj.TC_8_7_blog() 
    obj.tearDown() 

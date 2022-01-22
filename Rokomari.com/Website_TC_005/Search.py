import time 
from selenium import webdriver
from selenium.webdriver.common.by import By

baseUrl = 'https://www.rokomari.com/book'
driverpath = 'J:\Selenium\drivers\chromedriver.exe' 

class SearchClassTest():
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = driverpath)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window() 

    def search(self):
        self.driver.get(baseUrl)
        time.sleep(5)
        # Remove Pop-up message 
        self.driver.find_element(By.XPATH,'//*[@id="js--entry-popup"]/div[1]/button').click()
        time.sleep(2) 
        self.driver.find_element(By.ID,'js--search').click()
        self.driver.find_element(By.ID,'js--search').clear()
        self.driver.find_element(By.ID,'js--search').send_keys('Python')
        self.driver.find_element(By.XPATH,'//*[@id="js--main-header"]/div/div/div[2]/div/form/div/div/button').click()
        time.sleep(10)

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
        
if __name__ == '__main__':
    obj = SearchClassTest()
    obj.setUpClass()
    obj.search()
    obj.tearDown() 
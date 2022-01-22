import time 
from selenium import webdriver

baseUrl = 'https://www.flickr.com/'
driverpath = 'J:\Selenium\drivers\chromedriver.exe' 

class HomepageClassTest():
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = driverpath)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window() 

    def homepage(self):
        self.driver.get(baseUrl) 
        time.sleep(8) 

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
        
if __name__ == '__main__':
    obj = HomepageClassTest()
    obj.setUpClass()
    obj.homepage() 
    obj.tearDown() 




import time 
from selenium import webdriver

baseUrl = 'https://www.flickr.com/'
driverpath = 'J:\Selenium\drivers\chromedriver.exe' 

class SearchClassTest():
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = driverpath)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window() 

    def SearchTest(self):
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
        time.sleep(5) 
        #Click Search Button 
        self.driver.find_element_by_id('search-field').click()
        self.driver.find_element_by_id('search-field').send_keys("photos")
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/ul[2]/li[1]/div/form/label/input').click()
        time.sleep(10) 
        

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    obj = SearchClassTest()
    obj.setUpClass()
    obj.SearchTest() 
    obj.tearDown() 

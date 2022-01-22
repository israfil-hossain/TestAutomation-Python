import time 
from selenium import webdriver

baseUrl = 'https://www.flickr.com/'
driverpath = 'J:\Selenium\drivers\chromedriver.exe' 

class ProfileClassTest():
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
        time.sleep(5) 

    def TC_4_1_Upload_photo(self):
        # Click Profile button
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/ul[2]/li[4]/div/div/div/a/div').click()
        # Click Upload Photos
        self.driver.find_element_by_link_text("Upload your photos").click()
        time.sleep(3)
        # Click Choose Photos Button 
        # get file path
        file_path = 'J:\Selenium\Flicker.com\Website_TC_004\Profile\moto.jpg' 

        self.driver.find_element_by_id('choose-photos-and-videos').send_keys(file_path) 
        time.sleep(5) 
        # Update Button 
        self.driver.find_element_by_id("action-publish").click() 
        #Confirm Publish 
        self.driver.find_element_by_id("confirm-publish").click() 
        time.sleep(8) 
        self.driver.get(baseUrl)

    def TC_4_2_MailClassTest(self):
         
        time.sleep(4) 
        # Click Profile button
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/ul[2]/li[4]/div/div/div/a/div').click()
        # Click Mail Button
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div/section[3]/ul/li[1]/a').click()
        time.sleep(5)
        self.driver.get(baseUrl)

    def TC_4_3_SettingTest(self):

        # Click Profile button
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/ul[2]/li[4]/div/div/div/a/div').click()
        # Click Setting Button
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div/section[3]/ul/li[2]/a').click()
        time.sleep(4)
        self.driver.get(baseUrl)

    def TC_4_4_HelpTest(self):

        # Click Profile button
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/ul[2]/li[4]/div/div/div/a/div').click()
        # Click Help Button
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div/section[3]/ul/li[3]/a').click()
        time.sleep(4)
        self.driver.get(baseUrl)

    def TC_4_SignoutTest(self):
        time.sleep(4) 
        # Click Profile button
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/ul[2]/li[4]/div/div/div/a/div').click()
        # Click Help Button
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div/section[3]/ul/li[4]/a').click()
        time.sleep(10) 
    

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
        
if __name__ == '__main__':
    obj = ProfileClassTest()
    obj.setUpClass()
    obj.signin()
    obj.TC_4_1_Upload_photo() 
    obj.TC_4_2_MailClassTest()
    obj.TC_4_3_SettingTest()
    obj.TC_4_4_HelpTest()
    obj.TC_4_SignoutTest()
    obj.tearDown() 

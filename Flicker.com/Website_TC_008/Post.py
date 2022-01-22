import time 
from selenium import webdriver
from selenium.webdriver.common.by import By

baseUrl = 'https://www.flickr.com/'
driverpath = 'J:\Selenium\drivers\chromedriver.exe' 

class PostClassTest():
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = driverpath)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window() 

    def TC_8_1_PhotoSearch(self):
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
        self.driver.find_element_by_id('search-field').send_keys("Planet Stories Vol. 1, No. 9 ")
        time.sleep(3) 
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/ul[2]/li[1]/div/form/label/input').click()
        time.sleep(5) 
        self.driver.get('https://www.flickr.com/photos/57440551@N03/15847648542/in/photolist-q9pkMG-VGEoLc-2msiX4D-5YK2Je-2j1SNKo-2i8QH9J-2kLxr5q-2kLBT2g-7yQQHp-2kLBvgm-2kLBvf4-2kmYzth-2kmxXzs-2hBpzUY-2dgYuDq-2kLwVmN-2b95Cx9-2kLBKZa-2kLB6jy-2kLxjwf-2kLxf8f-2kLB9HH-2kLB9Hh-2kLBjc3-2kLBvh3-2kLxJqs-2kLBNNB-2kLB91B-2kLxbmT-2kLBd6p-2kLB93v-2kLwVgs-2kLBurB-2kLAQ7E-2kLB8ZE-2i8TeY8-2kLBt4F-2kLBmG2-2kLx6gc-2kLxf6G-2kLBDL3-2kLB3pv-2kLButW-2kLAQ8X-2kLB1TV-2kLBja9-2kLxJt8-2kLBvgB-2kLxJsr-2dgKFdC')

    def TC_8_2_PhotoLike(self):
        time.sleep(3)
        # remove popup msg 
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/a').click()
        time.sleep(2) 
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[5]/div[1]/div').click()
        time.sleep(5)

    def TC_8_3_PhotoaddtoGalary(self): 
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[5]/span').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div/div[3]/button').click()
        time.sleep(2) 
        self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys("Book")
        time.sleep(2)
        self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/textarea').send_keys('This is Book Galarry')
        time.sleep(2)
        self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/button[2]').click()
        time.sleep(4)

    def TC_8_4_PhotoShare(self):
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[5]/div[2]/div/span').click()
        time.sleep(4)
        self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div[1]').click()
        time.sleep(3) 

       
    
    def TC_8_5_PhotoDownload(self):
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[5]/div[3]').click()
        time.sleep(2)
        # self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[5]/div[3]').click()
        # time.sleep(3) 
        self.driver.find_element(By.XPATH,'/html/body/div[2]/div[1]').click()
        time.sleep(3) 
    
    def TC_8_6_PhotoComment(self):
        self.driver.find_element(By.NAME,'comment').send_keys("This is beautiful Book") 
        time.sleep(3)
        #Click Comment 
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[1]/div[1]/div[4]/div/button').click()
        time.sleep(3) 

    def TC_8_9_Follow(self):
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[1]/div[1]/div[1]/div/div/span/button/span').click()
        time.sleep(10) 


    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    obj = PostClassTest()
    obj.setUpClass()
    obj.TC_8_1_PhotoSearch()
    obj.TC_8_2_PhotoLike() 
    obj.TC_8_3_PhotoaddtoGalary() 
    obj.TC_8_4_PhotoShare()
    obj.TC_8_5_PhotoDownload()
    obj.TC_8_6_PhotoComment() 
    obj.TC_8_9_Follow()
    obj.tearDown() 

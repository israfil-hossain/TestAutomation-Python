import time 
from selenium import webdriver
from selenium.webdriver.common.by import By

baseUrl = 'https://www.rokomari.com/book'
driverpath = 'J:\Selenium\drivers\chromedriver.exe' 

class ProfileClassTest():
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

    def TC_4_1_My_account(self):
        # Click profile button 
        self.driver.find_element(By.XPATH,'/html/body/header/div/div/div/div/div[3]/div/div[3]/a').click()
        time.sleep(2)
        # click My account 
        self.driver.find_element(By.XPATH,'/html/body/header/div/div/div/div/div[3]/div/div[3]/div/a[1]').click()
        time.sleep(4)
        self.driver.find_element(By.ID,'js--edit-personal').click()
        time.sleep(2) 
        self.driver.find_element(By.NAME,'name').clear()
        self.driver.find_element(By.NAME,'name').send_keys('Israfil hossain')
        time.sleep(2) 
        self.driver.find_element(By.NAME,'dob').send_keys('08/13/1997')
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="my-account"]/div/div/div[2]/main/section/form[1]/div[3]/div[2]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/main/section/form[1]/input').click()
        time.sleep(5)
        self.driver.find_element(By.ID,'js--edit-mobile').click()
        self.driver.find_element(By.NAME,'phone').send_keys('01723560254')
        self.driver.find_element(By.XPATH,'//*[@id="phoneNumber"]').click()
        time.sleep(5)
        self.driver.find_element(By.ID,'js--change-email').click()
        self.driver.find_element(By.NAME,'email').send_keys('obujbalok467@gmail.com')
        self.driver.find_element(By.XPATH,'//*[@id="emailAddress"]').click()
        time.sleep(5)
        self.driver.find_element(By.ID,'js--edit-image').click()
        # get file path
        file_path = 'J:\Selenium\Flicker.com\Website_TC_004\Profile\moto.jpg'
        self.driver.find_element(By.XPATH,'//*[@id="photo"]').send_keys(file_path) 
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//*[@id="imageInfo"]').click()
        time.sleep(5) 


    def TC_4_2_My_Orders(self):
        # Click profile button 
        self.driver.find_element(By.XPATH,'/html/body/header/div/div/div/div/div[3]/div/div[3]/a').click()
        time.sleep(2)
        # click my orders 
        self.driver.find_element(By.XPATH,'/html/body/header/div/div/div/div/div[3]/div/div[3]/div/a[2]').click()
        time.sleep(5)

    def TC_4_3_My_List(self):
        # Click profile button 
        self.driver.find_element(By.XPATH,'/html/body/header/div/div/div/div/div[3]/div/div[3]/a').click()
        time.sleep(2)
        # click my list
        self.driver.find_element(By.XPATH,'/html/body/header/div/div/div/div/div[3]/div/div[3]/div/a[3]').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/main/section/div[1]/a/button').click()
        time.sleep(2) 
        self.driver.find_element(By.NAME,'nm').send_keys("Booklist") 
        time.sleep(2)
        self.driver.find_element(By.NAME,'dtl').send_keys("This is My BookList for Python and Programming")
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="products"]').send_keys('Python')
        # For manual select products 
        time.sleep(8)
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/main/section/div[2]/form/div[6]/input[2]').click() 
        time.sleep(5) 



    def TC_4_4_My_Wishlist(self):
        # Click profile button 
        self.driver.find_element(By.XPATH,'/html/body/header/div/div/div/div/div[3]/div/div[3]/a').click()
        time.sleep(2)
        # click Wishlist
        self.driver.find_element(By.XPATH,'/html/body/header/div/div/div/div/div[3]/div/div[3]/div/a[4]').click()
        time.sleep(5)

    def TC_4_5_My_rating(self):
        # Click profile button 
        self.driver.find_element(By.XPATH,'/html/body/header/div/div/div/div/div[3]/div/div[3]/a').click()
        time.sleep(2)
        # click Myrating review 
        self.driver.find_element(By.XPATH,'/html/body/header/div/div/div/div/div[3]/div/div[3]/div/a[5]').click()
        time.sleep(5)

    def TC_4_6_My_points(self):
        # Click profile button 
        self.driver.find_element(By.XPATH,'/html/body/header/div/div/div/div/div[3]/div/div[3]/a').click()
        time.sleep(2)
        # click points
        self.driver.find_element(By.XPATH,'/html/body/header/div/div/div/div/div[3]/div/div[3]/div/a[6]').click()
        time.sleep(5)

    def TC_4_7_Signout(self): 
        # Click profile button 
        self.driver.find_element(By.XPATH,'/html/body/header/div/div/div/div/div[3]/div/div[3]/a').click()
        time.sleep(2)
        # click signout 
        self.driver.find_element(By.XPATH,'/html/body/header/div/div/div/div/div[3]/div/div[3]/div/a[7]').click()
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
    # obj.TC_4_1_My_account() 
    obj.TC_4_2_My_Orders() 
    obj.TC_4_3_My_List() 
    obj.TC_4_4_My_Wishlist() 
    obj.TC_4_5_My_rating() 
    obj.TC_4_6_My_points() 
    obj.TC_4_7_Signout() 

    obj.tearDown() 

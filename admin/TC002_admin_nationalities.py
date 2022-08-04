import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/admin/nationality") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("admin") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # klik tombol sign in
        time.sleep(3)
    
    def test_a_tambahnationalities (self): 
        # steps
        browser = self.browser #buka web browser
        #mencari berdasarkan namanya
        browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[2]/div[1]/div[2]/form[1]/div[1]/input[1]").click() # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/ol[1]/li[1]/input[1]").send_keys("indonesia1") # klik tombol sign in
        time.sleep(3)
        browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/p[1]/input[1]").click()
        time.sleep(5)

  


    def test_a_hapusnationalities (self): 
        # steps
        browser = self.browser #buka web browser
        #mencari berdasarkan namanya
        browser.find_element(By.ID,"ohrmList_chkSelectRecord_219").click() # isi email
        time.sleep(3)
        browser.find_element(By.ID,"btnDelete").click()
        time.sleep(3)
        browser.find_element(By.ID,"dialogDeleteBtn").click()
        time.sleep(3)
    
        
        

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_cariuser (self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("admin") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # klik tombol sign in
        time.sleep(3)
        # validasi
        print("berhasil login")


        #mencari berdasarkan namanya
        browser.find_element(By.ID,"searchSystemUser_userName").send_keys("admin") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"searchBtn").click() # klik tombol sign in
        time.sleep(3)
        # validasi
        response_data =browser.find_element(By.ID,"resultTable").text
        self.assertNotEqual(response_data,"No Records Found")
        #Ngereset field nya 
        browser.find_element(By.ID,"resetBtn").click() # klik tombol sign in
        time.sleep(3)

        #mencari berdasarkan role nya 
        select = Select(browser.find_element(By.ID,"searchSystemUser_userType"))
        time.sleep(1)
        select.select_by_value('1')
        browser.find_element(By.ID,"searchBtn").click() # klik tombol sign in
        time.sleep(3)
        # validasi
        response_data =browser.find_element(By.ID,"resultTable").text
        self.assertNotEqual(response_data,"No Records Found")
        #Ngereset field nya 
        browser.find_element(By.ID,"resetBtn").click() # klik tombol sign in
        time.sleep(3)
          
    
   
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
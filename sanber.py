import unittest
import time
from unittest.mock import call
from urllib import response
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_success_login(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("admin") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi username # isi password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        print("berhasil login")
    
    def test_a_usermanagement_search_by_name(self): 
        # steps
        
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers ") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"searchSystemUser_userName").send_keys("admin1") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"searchBtn").click() # klik tombol search
        time.sleep(1)


        # validasi
        response_data = browser.find_element(By.ID,"frmList_ohrmListComponent").text

        self.assertIn('admin1', response_data)
       
 
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
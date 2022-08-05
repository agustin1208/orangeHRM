import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager


class myinfojob(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")
        browser.find_element(By.ID,"txtUsername").send_keys("admin") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # klik tombol sign in
        time.sleep(3)

    def test_a_assignLeave (self): 
        # steps
        browser = self.browser #buka web browser
        #mencari berdasarkan nama job nya
        browser.find_element(By.XPATH,"//body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]").click() # isi email
        time.sleep(1)

        response_data =browser.find_element(By.XPATH,"//input[@id='assignBtn']").text
        self.assertEqual(response_data,"")
        time.sleep(5)

    
        time.sleep(5)
     
        

       


    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()

    
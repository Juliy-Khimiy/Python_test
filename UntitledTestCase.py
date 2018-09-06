# -*- coding: utf-8 -*-
from selenium import webdriver
#import pyscreenshot as ImageGrab
import unittest

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("c:\\Program Files (x86)\\webdriver\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://192.168.1.65:3000/#/login/")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("yul56709081@gmail.com")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("111111")
        driver.find_element_by_id("login-button").click()
        driver.find_element_by_xpath("//button[contains(@ng-click, 'Root.onLogoutButtonClickEvent()')]").click()


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    #im = ImageGrab.grab(bbox=(10, 10, 300, 300))  # X1,Y1,X2,Y2
    #im.show()
    unittest.main()

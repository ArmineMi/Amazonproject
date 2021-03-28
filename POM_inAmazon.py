from selenium import webdriver
import time
import unittest
from IdeaProjects.Amazon1.HomeAmazon import HomeAmazon

class Amazon (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:/webdriver/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_Items(self):
        driver = self.driver
        driver.get("https://www.amazon.com/")
        home = HomeAmazon(driver)
        home.click_all()
        home.click_electronics()
        home.click_camera_photos()
        time.sleep(2)

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("OK")

    if __name__ == '__main__':
       unittest.main()
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomeAmazon():

    def __init__(self, driver):
        self.driver=driver
        self.all_icon_id= "nav-hamburger-menu"
        self.electronics_xpath= "//*[@id='hmenu-content']/ul[1]/li[7]/a"
        self.camera_photo_link_text= "Camera & Photo"

    def click_all(self):
        #self.driver.find_element_by_id("nav-hamburger-menu").click()
        element = WebDriverWait(self.driver, 20).until(lambda x:
                                               x.find_element_by_id("nav-hamburger-menu"))
        element.click()

    def click_electronics(self):
        #self.driver.find_element_by_xpath("//*[@id='hmenu-content']/ul[1]/li[7]/a").click()
        element = WebDriverWait(self.driver, 20).until(lambda x:
                                                       x.find_element_by_xpath("//*[@id='hmenu-content']/ul[1]/li[7]/a"))
        element.click()
    def click_camera_photos (self):
        #self.driver.find_element_by_link_text("Camera & Photos").click()
        element = WebDriverWait(self.driver, 20).until(lambda x:
                                                       x.find_element_by_link_text("Camera & Photo"))
        element.click()
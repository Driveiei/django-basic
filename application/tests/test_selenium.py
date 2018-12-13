from selenium import webdriver
from unittest import TestCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class UntitledTestCase(TestCase):
    def setUp(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"


    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://www.google.com/")
        driver.find_element_by_name("q").clear()
        driver.find_element_by_name("q").send_keys("home")
        driver.find_element_by_name("q").send_keys(Keys.ENTER)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Web results'])[1]/following::h3[1]").click()
        driver.find_element_by_link_text(u"บ้าน").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='บ้านเดี่ยว'])[1]/following::p[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='ประเภท'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='ทาวน์โฮม'])[2]/following::span[2]").click()
        Select(driver.find_element_by_id("type")
            ).select_by_visible_text(u"บ้านแฝด")
        self.assertTrue(True)

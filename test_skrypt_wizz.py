# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

valid_name = 'Dick'
valid_surname = 'Laurent'
valid_telephone = '123123123'
invalid_email = 'laurent.com'
valid_password = "qwerz12"


class WizzairRegistration(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://wizzair.com/pl-pl#/")

    def test_registration_invalid_email(self):
        driver=self.driver
        zaloguj_btn = driver.find_element_by_xpath('//*[@id="app"]/header/div[1]/div/nav/ul/li[7]/button')
        zaloguj_btn.click()
        sleep(3)
        rejestracja_btn = driver.find_element_by_css_selector('#login-modal > form > div > p > button')
        rejestracja_btn.click()
        imie_btn = driver.find_element_by_xpath('//input[@placeholder="Imię"]')
        imie_btn.send_keys(valid_name)
        nazwisko_btn = driver.find_element_by_xpath('//input[@placeholder="Nazwisko"]')
        nazwisko_btn.send_keys(valid_surname)
        sleep(3)
        plec_btn = driver.find_element_by_xpath('//*[@id="regmodal-scroll-hook-2"]/div[1]/label[2]/span')
#gdy zaslania nam cos przycisk mozemy wymusic java scriptem naciscienie przycisku,kod ponizej
        driver.execute_script("arguments[0].click()", plec_btn)
#       plec_btn.click()
        nr_tel_btn = driver.find_element_by_xpath('//*[@id="regmodal-scroll-hook-3"]/input')
        nr_tel_btn.send_keys(valid_telephone)
        sleep(3)
        email_btn = driver.find_element_by_xpath('//*[@id="regmodal-scroll-hook-4"]/div[1]/label/input')
        email_btn.send_keys(invalid_email)
        password_btn = driver.find_element_by_xpath('//*[@id="regmodal-scroll-hook-5"]/div[1]/label/input')
        password_btn.send_keys(valid_password)
        kraj_btn = driver.find_element_by_xpath('//*[@id="regmodal-scroll-hook-6"]/div[1]/label/input')
        kraj_btn.send_keys("Polska")
        kraj_btn.send_keys(Keys.RETURN)
        sleep(3)
    #    kraj_btn.send_keys("Polska")

    def teatDown():
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2)

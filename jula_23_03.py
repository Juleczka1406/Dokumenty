# -*- coding: utf-8 -*-
#!/usr/bin/python
#zaimportowanie niezbędnych bibliotek

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import unittest
#stwórz nowy sterownik do chrome
#driver = webdriver.Chrome()
#maksymalizuj okno
#driver.maximize_window()
#driver.get("http://www.wsb.pl")
#poczekaj 5 sek by nacieszyć oczy
#time.sleep(5)
#zamknij sterownik
#driver.quit()



#tworzę klasę WsbPlCheck dziedziczącą po klasie TestCase z modułu unittest
class WsbPlCheck(unittest.TestCase):
        #instrukcje, które zostaną wykonane przed każdym testem
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.get("http://www.wsb.pl")
        driver.maximize_window()

#tu będą wypisane nasze testy
#    def test_wsb_pl(self):
#        driver = self.driver
#        self.assertIn(u"Wyższe Szkoły Bankowe", driver.title)

#    def test_find_element_by_tag_name(self):
#        driver = self.driver
#        driver.find_element_by_tag_name("body")

#    def test_link(self):
#        driver = self.driver
#        link = self.driver.find_element_by_link_text(u"AKCEPTUJĘ")
#        link.click()
#        driver.implicitly_wait(10)

    def test_search(self):
        driver = self.driver
        driver.get("http://www.wsb.pl/chorzow/")
        pole = driver.find_element_by_id("edit-search-block-form--2")
        pole.send_keys("Tester")
        pole.send_keys(Keys.RETURN)
        driver.implicitly_wait(10)
        results = driver.find_elements_by_xpath('//*[@id="block-system-main"]/div/ol/li')

        print ("Znalazlem" + str(len(results)) + "wynikow:\n")
        for result in results:
            print(result.text + "/n")

        self.assertEqual(3, len(results))

    def tearDown(self):
        self.driver.quit()

if __name__== "__main__":
    unittest.main(verbosity = 2)

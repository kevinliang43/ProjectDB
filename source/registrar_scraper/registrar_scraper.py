from selenium import webdriver
from selenium.webdriver.support.select import Select
import os

# Constant Variables
CDRIVER_PATH = os.getcwd() + "/chromedriver"
URL = 'https://wl11gp.neu.edu/udcprod8/NEUCLSS.p_class_select#_ga=2.68357137.102712258.1526942415-989740985.1517584354'

# Create an instance of Chrome
#driver = webdriver.Chrome(CDRIVER_PATH)

# Get to the Course Registrar website
#driver.get(URL)


class registrar_navigator(object):

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(os.getcwd() + "/chromedriver")
        self.driver.get(self.url)
        self.options = {}

    def scrapeTermPage(self):
        self.select = Select(self.driver.find_element_by_xpath('//select[@name="STU_TERM_IN"]'))
        counter = 0
        for option in self.select.options:
            self.options[counter] = option.text
            counter = counter + 1
        del self.options[0] 

    def printOption(self):
        print "Please select an option: "
        counter = 1
        for option in self.options.values:
            print str(counter) + ". " + option
            counter = counter + 1

    def close(self):
        self.driver.close()
 
nav = registrar_navigator(URL)

nav.scrapeTermPage()
nav.printOption()
nav.close()

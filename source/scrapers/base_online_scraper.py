from bs4 import BeautifulSoup
import urllib

class base_online_scraper(object):

    def __init__(self, url):
        self.url = url

    def __setup(self): 
        fp = urllib.urlopen(self.url)
        soup = BeautifulSoup(fp, 'lxml')
        course_block = soup.find_all('div', class_="courseblock")
        return course_block

    def scrape(self):
        course_block = self.__setup()

        for course in course_block:
            # Scrape information from each course block
            courseCode, courseName, credits = course.find(
                                              'p', 
                                              class_="courseblocktitle"
                                              ).text.split(".", 2)
            courseDesc = course.find('p', class_="courseblockdesc").text
            
            # Clean up Strings
            courseName.strip(" ")
            credits.strip(" .")
            courseDesc.strip()
            print courseCode

URL = 'http://catalog.northeastern.edu/course-descriptions/acct/'

ACCT = base_online_scraper(URL)

ACCT.scrape()




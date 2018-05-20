from ProjectDB.classes import Course.py
from bs4 import BeautifulSoup
import urllib
import urlparse
import mechanize

URL = 'http://catalog.northeastern.edu/course-descriptions/acct/'

fp = urllib.urlopen(URL)
soup = BeautifulSoup(fp, 'lxml')
course_block = soup.find_all('div', class_="courseblock")


for course in course_block:
    # Scrape information from each course block
    courseCode, courseName, credits = course.find('p', class_="courseblocktitle").text.split(".", 2)
    courseDesc = course.find('p', class_="courseblockdesc").text
    
    # Clean up Strings
    courseName.strip(" ")
    credits.strip(" .")
    courseDesc.strip()
    print courseName   



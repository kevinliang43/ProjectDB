from bs4 import BeautifulSoup
import urllib
import urlparse
import mechanize

url = 'http://catalog.northeastern.edu/course-descriptions/acct/'

fp = urllib.urlopen(url)

soup = BeautifulSoup(fp, 'lxml')

# print soup.find_all('p')[0]
# print soup.find_all('p')[1]

course_block = soup.find_all('div', class_="courseblock")


for course in course_block:
    # Scrape information from each course block
    courseCode, courseName, credits = course.find('p', class_="courseblocktitle").text.split(".", 2)
    courseDesc = course.find('p', class_="courseblockdesc").text
    
    # Clean up Strings
    courseName.strip()
    credits.strip(" .")
    courseDesc.strip()
   


import bs4
import urllib

URL = 'http://catalog.northeastern.edu/course-descriptions/'

fp = urllib.urlopen(URL)
soup = bs4.BeautifulSoup(fp, 'lxml')
nav_menu = soup.find("div", {"id": "cl-menu"})
print nav_menu.text



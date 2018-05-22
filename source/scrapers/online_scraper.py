import bs4
import urllib
from base_online_scraper import base_online_scraper as scraper

BASE_URL = 'http://catalog.northeastern.edu'
INITIAL_PATH = '/course-descriptions/'

fp = urllib.urlopen(BASE_URL + INITIAL_PATH)
soup = bs4.BeautifulSoup(fp, 'lxml')
nav_menu = soup.find("div", {"id": "atozindex"}).find_all('a', href=True)

scraper = scraper('')

for a in nav_menu:
    scraper.url = BASE_URL + a['href']
    scraper.scrape()


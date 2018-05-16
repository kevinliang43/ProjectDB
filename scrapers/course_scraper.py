from bs4 import BeautifulSoup
import urllib
import urlparse
import mechanize

url = 'https://wl11gp.neu.edu/udcprod8/bwckctlg.p_disp_dyn_ctlg#_ga=2.217607510.1903761389.1526487460-989740985.1517584354'

browser = mechanize.Browser()
browser.open(url)

browser.select_form(nr=0)

form = browser.form

form['cat_term_in'] = ['201910'] 
new_url = browser.submit()

browser.open(new_url)

for link in browser.links():
    print link

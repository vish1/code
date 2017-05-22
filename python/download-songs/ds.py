
from bs4 import BeautifulSoup
import urllib2, pprint, re

def get_soup(url):
	response = urllib2.urlopen(url)
	return BeautifulSoup(response.read())

def get_hrefs(soup, pattern):
	return [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith(pattern)]

soup = get_soup('http://www.indiamp3.com/hindi-singer-artists-mp3')
hrefs = get_hrefs(soup, 'http://www.indiamp3.com/')

wanted = ['mahendra', 'rafi', 'hemant' , 'lata' , 'asha', 'manna', 'mukesh', 'parichay']
selected_hrefs = [href for want in wanted for href in hrefs if want in href]

final_hrefs = []
for sel in selected_hrefs:
	soup = get_soup(sel)
	hrefs = get_hrefs(soup, 'download-song')
	song_ids = [re.findall('\d+', href)[0] for href in hrefs]
	correct_hrefs = ['http://www.indiamp3.com/download.php?song_id=' + id for id in song_ids ]
	final_hrefs += correct_hrefs

with open('file_links', 'w') as f:
	for href in final_hrefs:
		f.write("%s\n" % href)

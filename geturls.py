#!/home/alive/projects/venv/geturls/bin/python
from sys import argv
from bs4 import BeautifulSoup
import requests

def geturls():
	url = argv[1]
	r = requests.get(url,{'User-agent':'mybot'})
	soup = BeautifulSoup(r.text,'html.parser')
	a = soup.find_all("a",{"href":True})
	for v in a:
		print v["href"]
if '__name__' == '__main__':
	geturls()

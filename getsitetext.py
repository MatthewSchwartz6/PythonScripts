import requests
from bs4 import BeautifulSoup

url = raw_input("Enter a URL: ")

print ("First here are a list of the URL's on this page:\n")

r = requests.get(url)
soup = BeautifulSoup(r.content,"html.parser")
links = soup.find_all('a')
for link in links:
	print (link.get('href'))
print("\nHere is the text from the site:\n")
print (soup.get_text())

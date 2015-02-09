import requests
import sys
from BeautifulSoup import BeautifulSoup

f = open('config.txt')
line = f.readline()
splitline = line.split(':')

username = splitline[0]
password = splitline[1].strip('\n')

payload = {
	'username': username,
	'password': password
}

with requests.Session() as c:
	r = c.post('https://m.website.com/login', data=payload)
	print r.status_code
	r = c.get('https://m.website.com/home')
	
	soup = BeautifulSoup(r.content)
	print soup.prettify()

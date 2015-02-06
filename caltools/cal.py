from BeautifulSoup import BeautifulSoup
import requests

config = open('config.txt', 'r')
url = ""

for line in config.readlines():
	if "#" in line:
		pass
	else:
		url = line.strip('\n')

r = requests.get(url)
soup = BeautifulSoup(r.text)

#print soup.prettify()

events = soup.findAll('title', {'type':'html'})
summaries = soup.findAll('summary', {'type':'html'})

for item in range(0,len(events)):
	event = events[item].contents
	print ''.join(event)
	summary = summaries[item].contents
	print ''.join(summary)
	print ''
	print ''
	print ''
	print ''


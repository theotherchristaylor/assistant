from BeautifulSoup import BeautifulSoup
import requests

config = open('config.txt', 'r')
positions = []

for line in config.readlines():
	if "#" in line:
		pass
	else:
		positions.append(line.strip('\n'))

for position in positions:
	url = 'https://www.google.com/finance?q=NYSEARCA:' + position
	r = requests.get(url)
	soup = BeautifulSoup(r.text)

	try:
		values = soup.find('div', {'class':'id-price-change nwp'}).span.span.contents
	except:
		try:
			values = soup.find('span', {'class':'id-price-change nwp'}).span.span.contents
		except:
			pass
	
	for x in values:
		print float(x)

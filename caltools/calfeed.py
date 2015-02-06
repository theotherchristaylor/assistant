import feedparser

config = open('config.txt', 'r')

for line in config.readlines():
	if '#' in line:
		pass
	else:
		url = line.strip('\n')

feed = feedparser.parse(url)

for entry in feed.entries:
	print entry.title
	print entry.summary



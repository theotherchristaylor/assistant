import feedparser

moviefeed = feedparser.parse('http://www.movies.com/rss-feeds/new-on-dvd-rss')

for entry in moviefeed.entries:
	print entry.title



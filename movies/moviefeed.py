import feedparser

moviefeed = feedparser.parse('http://www.fandango.com/rss/top10boxoffice.rss')

for entry in moviefeed.entries[0:-1]:
	title = entry.title
	splitmovie = title.split(' ')
	movie = splitmovie[1:-1]
	print ' '.join(movie)



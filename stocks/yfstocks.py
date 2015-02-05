from yahoo_finance import Share

positions = open('config.txt', 'r')

total_change = 0

for position in positions.readlines():
	if '#' in position:
		pass
	else:
		x = position.split(':')
		stock = Share(str(x[0]))
		change = float(stock.get_change().strip('+'))
		shares = float(x[1])
		
		total_change += (change * shares)

print("$%.2f" % round(total_change, 2))

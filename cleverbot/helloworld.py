import cleverbot
import sys

cb1 = cleverbot.Cleverbot()
print "POSE YOUR QUERY"

while 'pigs' != 'fly':
	sys.stdout.write('Me: ') 
	question = raw_input()
	if question == 'exit()':
		exit()
	sys.stdout.write('Cleverbot: ') 
	try:
		print cb1.ask(question)
	except Exception, e:
		print '[-] Error: ' + e



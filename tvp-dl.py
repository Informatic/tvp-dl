import urllib2, json, sys, re
url = sys.argv[1]

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')]

def p(i):
	sys.stderr.write(' ~ initsession\n')
	opener.open('http://www.tvp.pl/pub/sess/initsession').read()
	sys.stderr.write(' ~ viewrequest\n')
	opener.open('http://www.tvp.pl/pub/sess/viewrequest?object_id='+str(i)).read()
	sys.stderr.write(' ~ getting download URL...\n')
	d = opener.open('http://www.tvp.pl/shared/cdn/tokenizer_v2.php?object_id='+str(i)+'&sdt_version=2').read()
	j = json.loads(d)
	
	#print j
	
	if 'url' in j and j['url'].strip() != '':
		print j['url']
	else:
		sys.stderr.write('\033[1m\033[41m ! Error occured:\033[0m\n%s\n' % (j,))
		exit(1)

if url.isdigit(): # Someone has just provided video_id.
	p(url)

elif re.findall('^.*\/(\d+)$', url): # URL provided ends with number (probably main tvp.pl site URL)
	try:
		opener.open(url).read()
	except:
		sys.stderr.write(" ! Couldn't load page [%s], continuing..." % (sys.exc_info(),))
	i = re.findall('^.*\/(\d+)$', url)[0]
	sys.stderr.write(' ~ assuming vidid=%s\n' % (i,))
	p(i)

else: # Something different. For example londyn2012.tvp.pl We've got to look for video_id=XXX
	sys.stderr.write(' ~ reading page and looking for video_id...\n')
	d = opener.open(url).read()
	r = re.findall('video_id=(\d+)', d)
	if not len(r):
		sys.stderr.write(" ! Shit broke. No video_id's found.\n")
		exit(1)
	
	else:
		sys.stderr.write(" ~ Found %d video_id's: %s. Assuming first.\n" % (len(r), ', '.join(r)))
		
		p(r[0])

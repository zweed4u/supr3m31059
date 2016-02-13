import urllib2, json, time

mobileStockURL='http://www.supremenewyork.com/mobile_stock.json'

def mobileReq():
	req = urllib2.Request(mobileStockURL)
	req.add_header('User-Agent','Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_4 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B350 Safari/8536.25')

	resp = urllib2.urlopen(req)
	data = json.loads(resp.read())

	print "\nCategories:"
	numCat=1

	for item in [x.encode('UTF8') for x in data[u'products_and_categories'].keys()]:
		print str(numCat)+": "+item
		numCat+=1

	choice = raw_input("\nWhich category do you wish to parse? (number) ")
	count=0
	numOfItems=len(data[u'products_and_categories'][data[u'products_and_categories'].keys()[int(choice)-1]])
	print '\n'

	while count < numOfItems:
		print data[u'products_and_categories'][data[u'products_and_categories'].keys()[int(choice)-1]][count][u'name'] + " :: " + "http://www.supremenewyork.com/shop/"+str(data[u'products_and_categories'][data[u'products_and_categories'].keys()[int(choice)-1]][count][u'id'])
		count+=1

	print '\n'
while 1:
	mobileReq()
	print "\n\n\n\n SLEEPING FOR 5 SECONDS \n\n\n\n"	
	time.sleep(5)


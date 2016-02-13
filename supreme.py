import urllib, urllib2, json, time, datetime, requests
class text:
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'


#keyword lowercase!!!!
keyword=raw_input("Product name? ")

req = urllib2.Request('http://www.supremenewyork.com/mobile_stock.json')
req.add_header('User-Agent', "User-Agent','Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_4 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B350 Safari/8536.25")
resp = urllib2.urlopen(req)
data = json.loads(resp.read())
numOfNew=len(data[u'products_and_categories'][u'new'])
print numOfNew
for i in range(numOfNew):
	productName=data[u'products_and_categories'][u'new'][i] [u'name']
	skuId=str(data[u'products_and_categories'][u'new'][i][u'id'])
	if keyword in productName.lower():
		indexOfDesired=i;
		#print i;
		break;#will increment up to desired then break
	else:
		#loop - keyword not found jump or reload data with json
		print "Sorry, item not found in json."
		if (i==numOfNew):
			print "end of list of products"
		else:
			print ''
			#still keep searching
	#all new products and skus
	#print productName+" :: " +skuId

nameProd=data[u'products_and_categories'][u'new'][indexOfDesired][u'name']
sizeId=str(data[u'products_and_categories'][u'new'][indexOfDesired][u'id'])
print nameProd+ " :: " + sizeId

jsonurl = 'http://www.supremenewyork.com/shop/'+str(data[u'products_and_categories'][u'new'][indexOfDesired][u'id'])+'.json'

response = urllib.urlopen(jsonurl)
while response.geturl() =='http://www.supremenewyork.com/shop':
	time.sleep(1)
	response = urllib.urlopen(jsonurl)
	print str(datetime.datetime.now())+": "+response.geturl()

response = urllib.urlopen(jsonurl)	
data = json.loads(response.read())
#print data
print '\n';
count=0;
#enumerate how many colors
numcolorways=len(data.values()[0])
chooseColor=[];
chooseSize=[];
for i in range(numcolorways):
	cwinfo=(data.values()[0][i]) 
	print str(i) + '.) ' +text.UNDERLINE+text.BOLD+str(cwinfo[u'name'])+" :: " + str(cwinfo[u'id'])+text.END
	chooseColor.append(str(cwinfo[u'name'])) #array choice - 1 indexing
	numsizes=len(cwinfo[u'sizes'])
	for j in range(numsizes):
		print '---'+str(count)+'.)  '+str(cwinfo[u'sizes'][j][u'name'].rjust(6)) +" :: " + str(cwinfo[u'sizes'][j][u'id']) + " :: Qty. "+str(cwinfo[u'sizes'][j][u'stock_level']) + ' -- \n'
		chooseSize.append(str(cwinfo[u'sizes'][j][u'id']));
		count+=1;
	print ""

#colorIndex=raw_input("Color index? ")  - not really needed
sizeIndex=raw_input("Size index? ")
#print colorIndex+ ' -- '+chooseColor[int(colorIndex)]
print sizeIndex+ ' -- '+chooseSize[int(sizeIndex)]

formQueriedURL='http://www.supremenewyork.com/shop/'+sizeId+'/add'
session=requests.Session()

#Payload --- scrape for auth token down here or recent one
data={'utf8': '%E2%9C%93',
	  'authenticity_token': 'oBLLJkW+A2plgT1lUJeKXq7DdqJSniGnZhnSmpuAQOE%3D',
	  'size': str(chooseSize[int(sizeIndex)]),
	  'commit': 'add+to+cart'}

session.cookies.clear()
response=session.post(formQueriedURL,data=data)
cartResponse=session.request('get','http://www.supremenewyork.com/shop/cart')
print '\n'
#print cart page's html for viewing cart on practiceboard.com
print cartResponse.content
print '\n'
print type(cartResponse.cookies)
print '\n'
print cartResponse.cookies
print '\n'
print session.cookies.get_dict()
#transfer cartResponse's cookies to webdriver/browser





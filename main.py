import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import math

#math rounding
def roundup(x):
    return int(math.ceil(x / 100000.0)) * 100000

#import URL
urlinput = input("enter url: ")
#url = "https://stockx.com/adidas-yeezy-boost-350-v2-beluga-2-0"
url = urlinput
print('url entered ' + url)
print('Processing Site')
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
g_name = []
g_name = soup.find_all("h1",{"class": "name"})
g_data = soup.find_all("div", {"class": "market-summary"})
for item in g_data:
	g_size = item.contents[0].find_all("div", {"class": "inset"})
print('Building Data')


#DATA SET LOOP
records = []
for result in g_size:
	#format size (add "(PO)")
	size = result.contents[0].text
	try:
		size = ''.join(size)
		ussize = [sizes for sizes in size + " (PO)"]
		ussize = ''.join(ussize)
	except:
		ussize = ""
	#format price + formula
	price = result.contents[1].text.replace('$','')	
	price = ''.join(price)
	try:
		price = int(price)
		idr = (price+55)*1.10*13500
		idr = roundup(idr)
	except:
		idr = ""
	records.append((ussize,idr))


#DATABASE & EXPORT

df = pd.DataFrame(records, columns=['size','price'])
'''
df["D"] = np.nan
df = pd.DataFrame(records[0], columns=['price'])'''
print('Generating File')
nameinput = input("Enter File Name(without file ext.): ")
filename = nameinput +'.csv'
df.to_csv(filename ,index=False,encoding='utf-8')
print('done')


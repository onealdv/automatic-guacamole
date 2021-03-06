# Things to do:
# - automatically update
# - do something about PO products (write name with (PO) and use fixed price)
# - do something about products that are ready stock(include ready stock and add 'ready' tag)


import requests
from bs4 import BeautifulSoup
#import pandas as pd
import numpy as np
import math
import csv
import gc
from aiohttp import ClientSession
import asyncio
import concurrent.futures
from selenium import webdriver
import time
import sys
import csv
import json

handlelist = []
sizelist = []
pricelist = []
emptylist = []
titlelist = []
bodylist = ['<meta charset="utf-8"> <div class="title"> <meta charset="utf-8"> <div class="Trust__container__3bA3U" data-reactid="115"> <div class="Trust__image-container__3yIDD" data-reactid="116"><img src="https://www.goat.com/images/products/icon_verification@2x.png" width="30" height="30" class="Trust__image__3gb_e" data-reactid="117"></div> <div class="Trust__title__3cC5B" data-reactid="118"><strong>1000% AUTHENTIC</strong></div> <div class="Trust__desc__32B5p" data-reactid="119"> <p class="p1">Semua sneaker dari VTL melewati LEGIT CHECK oleh tim profesional untuk memastikan keaslian sneaker tersebut.</p> <p class="p1"> </p> </div> </div> <div class="Trust__container__3bA3U" data-reactid="120"> <div class="Trust__image-container__3yIDD" data-reactid="121"><img src="https://www.goat.com/images/products/icon_return@2x.png" width="30" height="30" class="Trust__image__3gb_e" data-reactid="122"></div> <div class="Trust__title__3cC5B" data-reactid="123"><strong>RETURNS</strong></div> <div class="Trust__desc__32B5p" data-reactid="124">Kami menerima pengembalian barang pada Brand New sneakers yang tetap dalam kondisi yang sama seperti yang dikirim. Kami akan memberikan <em>refund</em> untuk jumlah yang telah dibayar (di kurang biaya pengiriman) dalam bentuk <em>store credit</em>. Mohon hubungi kami untuk info lebih lanjut.</div> </div> </div>']
vendorlist = ['Vendor']

publishlist = ['TRUE']
option1name = ['Size']
variantgrams = ['2000']
varianttrack = ['shopify']
variantqty = []
variantpolicy = ['deny']
variantfull = ['manual']
variantreq = ['TRUE']
varianttax = ['FALSE']
variantweight = ['kg']
giftcardlist = ['FALSE']

urllist = []
stockximg = []
namekey = []
lendict = {}
with open('prodlist.csv','r') as fin:
    csvreader = csv.reader (fin,delimiter =',')
    for line in csvreader:
        for entry in line :
            #print("Getting image URL")
            if entry not in urllist:
                if entry != '':
                    urllist.append(entry)
urllist = sorted(urllist)
for entry in urllist:
    print(entry)

def geturl():
    alist= ['https://stockx.com/adidas/most-popular','https://stockx.com/adidas','https://stockx.com/retro-jordans','https://stockx.com/retro-jordans/most-popular','https://stockx.com/nike','https://stockx.com/nike/most-popular','https://stockx.com/nike/top-selling','https://stockx.com/supreme/sweatshirts/top-selling','https://stockx.com/other-sneakers/most-popular','https://stockx.com/kith','https://stockx.com/kith/most-popular','https://stockx.com/kith/top-selling','https://stockx.com/supreme/accessories/most-popular','https://stockx.com/supreme/accessories','https://stockx.com/supreme/headwear','https://stockx.com/supreme/headwear/most-popular','https://stockx.com/supreme/headwear/most-expensive','https://stockx.com/supreme/jackets/most-expensive','https://stockx.com/supreme/jackets','https://stockx.com/supreme/jackets/most-popular','https://stockx.com/supreme/t-shirts/most-popular','https://stockx.com/supreme/t-shirts','https://stockx.com/supreme/t-shirts/top-selling','https://stockx.com/supreme/t-shirts/most-expensive','https://stockx.com/supreme/sweatshirts/most-expensive','https://stockx.com/supreme/sweatshirts','https://stockx.com/supreme/sweatshirts/most-popular']

    for url in alist:
        driver = webdriver.Chrome()
        driver.get(url)
        #time.sleep(5)
        htmlSource = driver.page_source
        driver.close()

        soup = BeautifulSoup(htmlSource,'html.parser')

        links = soup.find_all("a",{"class":"tile browse-tile"})
        newlist = []
        oldlist = []
        for url in links:
            handles = url.get("href")
            newlist.append('https://stockx.com'+handles)
        with open ('prodlist.csv','r') as fin:
            reader = csv.reader(fin)
            for line in reader:
                for entry in line:
                    oldlist.append(entry)
        finallist = list(set(newlist+oldlist))
        csvlinks = ','.join(newlist)
        with open ('prodlist.csv','w') as fout:
            writer = csv.writer(fout)
            writer.writerow(finallist)


def openfile(filename):
    with open(filename, 'r') as file:
        a = file.readlines()
        prodlist = []
        for line in a[1:]:
            a = line.split(';')
            if a[0] in prodlist:
                pass
            else:
                prodlist.append(a[0])
        # a= ''.join(prodlist)
    with open('prodlist.csv','w') as fout:
        csvwriter = csv.writer(fout)
        csvwriter.writerow(prodlist)

def roundup(x): #math rounding
    return int(math.ceil(x / 100000.0)) * 100000


#Request all links.
async def fetch(url, session):
    try:
        async with session.get(url) as response:
            return await response.read()
    except:
        print(f"failed at {url} {type(url)}")


async def run(r):

    tasks = []
    async with ClientSession() as session:
        num = 0
        for i in range(len(urllist)):
            task = asyncio.ensure_future(fetch(urllist[i], session))
            tasks.append(task)
            num+= 1

        responses = await asyncio.gather(*tasks)
        print(f"Total task: {len(responses)}")
        # you now have all response bodies in this variable


    with open('export.csv','w',newline= '') as fout:
                    writer = csv.writer(fout)
                    writer.writerow(['Handle', 'Title', 'Body (HTML)', 'Vendor', 'Type', 'Tags', 'Published', 'Option1 Name', 'Option1 Value', 'Option2 Name', 'Option2 Value', 'Option3 Name', 'Option3 Value', 'Variant SKU', 'Variant Grams', 'Variant Inventory Tracker', 'Variant Inventory Qty', 'Variant Inventory Policy', 'Variant Fullfilment Service', 'Variant Price', 'Variant Compare', 'Variant Requires Shipping', 'Variant Taxable', 'Variant Barcode', 'Image Src', 'Image Position', 'Image Alt Text', 'Gift Card', 'SEO Title', 'SEO Description', 'Google Shopping / Google Product Category', 'Google Shopping / Gender', 'Google Shopping / Age Group', 'Google Shopping / MPN', 'Google Shopping / AdWords Grouping', 'Google Shopping / AdWords Labels', 'Google Shopping / Condition', 'Google Shopping / Custom Product', 'Google Shopping / Custom Label 0', 'Google Shopping / Custom Label 1', 'Google Shopping / Custom Label 2', 'Google Shopping / Custom Label 3', 'Google Shopping / Custom Label 4', 'Variant Image', 'Variant Weight Unit', 'Variant Tax Code'])

    with open ('instock.json','r') as fin:
        jsondata = json.load(fin)
    succeed = 0
    failed = 0
    for i in range(len(responses)):
        # try:
        soup = BeautifulSoup(responses[i], "html.parser")
        g_name = soup.find("h1",{"class": "name"})
        g_data = soup.find_all("div", {"class": "market-summary"})
        for item in g_data:
            g_size = item.contents[0].find_all("div", {"class": "inset"})
        name = g_name.text.split()
        print(urllist[i])
        handleinput = urllist[i].split('/')[3]
        imglist = []
        imgpos = []

        lendictval = 0
        ready = 0

        try:
            ready1 = jsondata[handleinput]
            for entry in ready1:
                handlelist.append(handleinput)
                sizelist.append(entry['size'])
                pricelist.append(entry['price'])
                variantqty.append(entry['quantity'])
                lendictval+=1
                if entry['quantity'] != 0:
                    ready = 1
        except:
            pass

        titlelist.append(g_name.text)



        #get img url
        print(f"Formatting data for {g_name.text}")
        g_sku = soup.find_all("div",{"class":{"detail"}})
        sku = str(g_sku[0].contents[1]).split()[1]
        if sku == 'TBD':
            url2 = f'https://www.stadiumgoods.com/search/go?w={g_name.text}'
        else:
            url2 = f'https://www.stadiumgoods.com/search/go?w={sku}'

        if ready >0:
            taginput = ','.join(name)+','+sku.strip()+',ready'
        else:
            taginput = ','.join(name)+','+sku.strip()
        taglist = [taginput]
        r2 = requests.get(url2, stream = True)
        soup2 = BeautifulSoup(r2.content,"html.parser")
        g_file = soup2.find_all("div",{"class":{"product-gallery-image"}})
        #stockximg.append(str(g_file.contents).split('"')[5])
        namekey.append(g_name.text)



        imgposition = 1
        for item in g_file:
            g_img = item.contents
            a = str(g_img[1]).split()
            counter = 0
            for i in a:
                if i == 'itemprop="image"':
                     imglist.append(a[counter+1].split('"')[1])
                     imgpos.append(imgposition)
                     imgposition+=1
                else:
                    counter +=1
        if imglist == []: #if not found in stadiumgoods
            # r = requests.get(url, stream = True)
            # soup = BeautifulSoup(r.content,"html.parser")
            g_file = soup.find("div",{"class":{"full"}})
            print(str(g_file.contents).split('"')[5])
            if len(str(g_file.contents).split('"')[5]) < 60:
                g_link = soup.find("div",{"class":{'image-container'}})
                imglist.append(str(g_link.contents).split('"')[5])
                imgpos.append(imgposition)
                imgposition+=1
            else:
                imglist.append(str(g_file.contents).split('"')[5])
                imgpos.append(imgposition)
                imgposition+=1
            # try:
            #     print(a.index('https://stockx-360.imgix.net/Air-Jordan-4-Retro-White-Cement-2016_TruView/Images/Air-Jordan-4-Retro-White-Cement-2016_TruView/Lv2/img26.jpg?auto=format,compress&amp;w=1117&amp;q=40'))
            # except:
            #     print('not there')



#Data list




        #format csv file
        print("Formatting CSV file")
        for result in g_size:
            size = result.contents[0].text
            price = result.contents[1].text.replace('$','')
            price = ''.join(price)

            if price != 'Bid' and size != "All" and price != '' and size != '': #excludes empty price and "all" size entry

                try:
                    size = ''.join(size)
                    ussize = [sizes for sizes in size + " (PO)"] #format size (add "(PO)")
                    ussize = ''.join(ussize)
                except:
                    ussize = ""
                sizelist.append(ussize)
                if int(price) > 500:
                    try:
                        price = int(price)
                        idr = (price+55)*1.08*13800 #format price + formula
                        idr = roundup(idr)

                    except:
                        idr = ""
                else:
                    try:
                        price = int(price)
                        idr = (price+55)*1.1*13800 #format price + formula
                        idr = roundup(idr)

                    except:
                        idr = ""
                pricelist.append(idr)


        while len(imglist)>len(sizelist):
            sizelist.append('')
        while len(sizelist) > len(imglist):
            imglist.append('')
        while len(sizelist) > len(imgpos):
            imgpos.append('')
        while len(sizelist)>len(namekey):
            namekey.append('')
        while len(sizelist)>len(pricelist):
            pricelist.append('')
        while len(sizelist)>len(bodylist):
            bodylist.append('')
        while len(sizelist)>len(emptylist):
            emptylist.append('')
        while len(sizelist)>len(vendorlist):
            vendorlist.append('')
        while len(sizelist)>len(publishlist):
            publishlist.append('')
        while len(sizelist)>len(option1name):
            option1name.append('')
        while len(sizelist)>len(emptylist):
            emptylist.append('')
        while len(sizelist)>len(variantgrams):
            variantgrams.append('')
        while len(sizelist)>len(varianttrack):
            varianttrack.append('')
        while len(sizelist)>len(variantqty):
            variantqty.append('')
        while len(sizelist)>len(variantpolicy):
            variantpolicy.append('')
        while len(sizelist)>len(variantfull):
            variantfull.append('')
        while len(sizelist)>len(variantreq):
            variantreq.append('')
        while len(sizelist)>len(varianttax):
            varianttax.append('')
        while len(sizelist)>len(variantweight):
            variantweight.append('')
        while len(sizelist)>len(giftcardlist):
            giftcardlist.append('')
        while len(sizelist)>len(handlelist):
            handlelist.append(handleinput)
        while len(sizelist)>len(titlelist):
            titlelist.append('')
        while len(sizelist)>len(taglist):
            taglist.append('')
        while len(sizelist)>len(publishlist):
            publishlist.append('')


        d = {'Handle': handlelist, 'Title': titlelist, 'Body (HTML)': bodylist, 'Vendor': vendorlist, 'Type': vendorlist, 'Tags': taglist, 'Published':publishlist, 'Option1 Name':option1name, 'Option1 Value':sizelist, 'Option2 Name':emptylist,'Option2 Value': emptylist, 'Option3 Name': emptylist, 'Option3 Value':emptylist,'Variant SKU': emptylist, 'Variant Grams': variantgrams, 'Variant Inventory Tracker': varianttrack, 'Variant Inventory Qty': variantqty, 'Variant Inventory Policy': variantpolicy, 'Variant Fullfilment Service':variantfull, 'Variant Price': pricelist, 'Variant Compare': emptylist, 'Variant Requires Shipping': variantreq, 'Variant Taxable': varianttax, 'Variant Barcode': emptylist, 'Image Src': imglist, 'Image Position': imgpos, 'Image Alt Text': emptylist, 'Gift Card': giftcardlist, 'SEO Title': emptylist, 'SEO Description': emptylist, 'Google Shopping / Google Product Category': emptylist,'Google Shopping / Gender':emptylist, 'Google Shopping / Age Group':emptylist,'Google Shopping / MPN':emptylist,'Google Shopping / AdWords Grouping':emptylist,'Google Shopping / AdWords Labels':emptylist,'Google Shopping / Condition':emptylist,'Google Shopping / Custom Product':emptylist,'Google Shopping / Custom Label 0':emptylist,'Google Shopping / Custom Label 1':emptylist,'Google Shopping / Custom Label 2':emptylist,'Google Shopping / Custom Label 3':emptylist,'Google Shopping / Custom Label 4':emptylist,'Variant Image':emptylist,'Variant Weight Unit':variantweight,'Variant Tax Code':emptylist}
        dlist = list(d.values())

        print("Exporting")
        #print(dlist[0:2])
        with open('export.csv','a',newline= '') as fout:
            writer = csv.writer(fout)
            for i in range(len(d['Handle'])):
                newlist = []
                for entry in dlist:
                    try:
                        print('Success')
                        newlist.append(entry[i])
                        # print(len(entry))
                        # print(len(d['Handle'])-1)
                    except:
                        print(len(entry))
                        pass
                        #print(f"Failed at {entry}")
                writer.writerow(newlist)
        succeed +=1
    # # except:
    #     print(f'Failed to extract {urllist[i]}')
    #     failed +=1
    print(f"Succeeded {succeed} products")
    print(f"Failed {failed} products")

    #         with open('prodlistfail.txt','a') as fout:
    #             fout.write(handleinput)
    #             fout.write('\n')
    # #gc.collect()


# def errorchecker():
#     with open('prodlist.csv','r') as fin:
#         csvreader = csv.reader (fin,delimiter =',')
#         for line in csvreader:
#             for entry in line :
#                 url = 'https://stockx.com/'+entry
#                 print(f"Processing {url}")
#                 resp = requests.get(url)
#                 print("Getting Error code")
#                 code = resp.status_code
#                 i = 1
#                 if code == 400:
#                     print(f"Found {i} error links")
#                     i+=1
#                     with open('prodlistfail.txt','w') as fout:
#                         fout.write('https://stockx.com/'+entry)
#                 gc.collect()
exportlist = []
def clean():

    with open('export.csv','r') as fin:
        csvreader = csv.reader(fin,delimiter = ',')
        #exportlist = [x for x in csvreader if x!=[]]
        for x in csvreader:
            if x != []:
                exportlist.append(x)
        # a = [','.join(entry) for entry in exportlist]
        # print(len(a))
        #a = ''.join(exportlist)
    with open('export.csv','w') as fout:
        csvwriter = csv.writer(fout)
        for entry in exportlist:
            csvwriter.writerow(exportlist)


def cleanupfile():
    with open ('prodlistfail.txt','r') as fin:
        content = fin.readlines()
        content = [x.strip() for x in content]
    with open('prodlist.csv','r') as fin:
        csvreader = csv.reader (fin,delimiter =',')
        #prodlist = [line for line in csvreader]
        prodlist = []
        for line in csvreader:
            for entry in line:
                prodlist.append('https://stockx.com/'+entry)

    with open('prodlist.csv','w') as fout:
        faillist = [entry for entry in content]
        for fail in faillist:
            for entry in prodlist:
                if fail == entry:
                    prodlist.remove(fail)
        csvwriter = csv.writer(fout)
        csvwriter.writerow(prodlist)


if __name__ == '__main__':
    number = 1
    while True:
        print("Starting program")
        #geturl()
        #openfile('products_export.csv')
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(run(len(urllist)))
        loop.run_until_complete(future)
        #cleanupfile()
        #clean()
        print(f"Done {number}")
        number+=1
        time.sleep(86400)




# Things to do:
# - automatically update
# - do something about PO products (write name with (PO) and use fixed price)
# - do something about products that are ready stock(include ready stock and add 'ready' tag)

#fix imgpos
#fix getimg url


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
import selenium
from selenium import webdriver
import time
import sys
import csv
import json
from collections import OrderedDict
import pprint
import re
from datetime import datetime

urllist = []



skulist = []
imglist = []
imgpos = []
stockximg = []
namekey = []
sizelist = []
pricelist = []
emptylist = []
bodylist = [ ]
vendorlist = []
publishlist = []
option1name = []
variantgrams = []
varianttrack = []
variantqty = [ ]
variantpolicy = []
variantfull = []
variantreq = []
varianttax = []
variantweight = []
giftcardlist = []
handlelist = []
titlelist = []
taglist = []
lendict = {}
htmllist = []
imgdict = {}
sghtml = []
stockxdict = {}

def geturl():
    #alist= ['https://stockx.com/adidas/most-popular','https://stockx.com/nike/basketball','https://stockx.com/nike/footwear','https://stockx.com/nike/lebron','https://stockx.com/nike/air-force','https://stockx.com/nike/kobe','https://stockx.com/nike/foamposite','https://stockx.com/nike/sb','https://stockx.com/adidas','https://stockx.com/retro-jordans','https://stockx.com/retro-jordans/most-popular','https://stockx.com/nike','https://stockx.com/nike/most-popular','https://stockx.com/nike/top-selling','https://stockx.com/other-sneakers/most-popular','https://stockx.com/supreme/accessories/most-popular','https://stockx.com/supreme/accessories','https://stockx.com/supreme/headwear','https://stockx.com/supreme/headwear/most-popular','https://stockx.com/supreme/headwear/most-expensive']
    #alist= ['https://stockx.com/retro-jordans/packs',https://stockx.com/sneakers/most-popular',https://stockx.com/kith/t-shirts/highest-bid','https://stockx.com/kith/t-shirts/lowest-ask','https://stockx.com/kith/t-shirts/price-premium','https://stockx.com/kith/t-shirts/most-expensive','https://stockx.com/kith/t-shirts/most-popular','https://stockx.com/kith/t-shirts','https://stockx.com/supreme/jackets/price-premium','https://stockx.com/kith/jackets','https://stockx.com/kith/bottoms/most-expensive','https://stockx.com/kith/bottoms','https://stockx.com/supreme/t-shirts/highest-bid','https://stockx.com/supreme/t-shirts/price-premium','https://stockx.com/supreme/t-shirts/top-selling','https://stockx.com/supreme/t-shirts/most-expensive','https://stockx.com/supreme/t-shirts/most-popular','https://stockx.com/supreme/t-shirts','https://stockx.com/supreme/bags/most-expensive','https://stockx.com/supreme/bags','https://stockx.com/supreme/sweatshirts/top-selling','https://stockx.com/supreme/sweatshirts/most-expensive','https://stockx.com/supreme/sweatshirts/price-premium','https://stockx.com/supreme/sweatshirts','https://stockx.com/supreme/jackets/most-expensive','https://stockx.com/supreme/jackets','https://stockx.com/supreme','https://stockx.com/supreme/accessories/most-popular','https://stockx.com/supreme/accessories','https://stockx.com/supreme/headwear','https://stockx.com/supreme/headwear/most-popular','https://stockx.com/supreme/headwear/most-expensive','https://stockx.com/nike/air-max/most-popular','https://stockx.com/nike/air-max','https://stockx.com/other-sneakers/asics/most-popular','https://stockx.com/other-sneakers/asics/most-expensive','https://stockx.com/other-sneakers/asics','https://stockx.com/retro-jordans/price-premium','https://stockx.com/retro-jordans/recent-asks','https://stockx.com/retro-jordans/highest-bid','https://stockx.com/retro-jordans','https://stockx.com/adidas/nmd/lowest-ask','https://stockx.com/adidas/nmd/top-selling','https://stockx.com/adidas/nmd/price-premium','https://stockx.com/adidas/nmd/most-expensive','https://stockx.com/adidas/nmd/most-popular','https://stockx.com/adidas/nmd','https://stockx.com/adidas/ultra-boost/highest-bid','https://stockx.com/adidas/ultra-boost/price-premium','https://stockx.com/adidas/ultra-boost/most-popular','https://stockx.com/adidas/ultra-boost','https://stockx.com/adidas/yeezy','https://stockx.com/adidas/most-popular','https://stockx.com/nike/basketball','https://stockx.com/nike/footwear','https://stockx.com/nike/lebron','https://stockx.com/nike/air-force','https://stockx.com/nike/kobe','https://stockx.com/nike/foamposite','https://stockx.com/nike/sb','https://stockx.com/adidas','https://stockx.com/retro-jordans','https://stockx.com/retro-jordans/most-popular','https://stockx.com/nike','https://stockx.com/nike/most-popular','https://stockx.com/nike/top-selling','https://stockx.com/other-sneakers/most-popular']
    #searchlist = ['https://stockx.com/search?s=supreme%20chicken%20dinner','https://stockx.com/search?s=nmd%20r1','https://stockx.com/search?s=nmd%20r2','https://stockx.com/search?s=ultraboost%204.0','https://stockx.com/search?s=ultraboost%203.0','https://stockx.com/search?s=ultraboost%201.0','https://stockx.com/search?s=ultraboost%202.0','https://stockx.com/search?s=supreme%20fire%20tee','https://stockx.com/search?s=supreme%20jelylfish','https://stockx.com/search?s=supreme%20independent','https://stockx.com/search?s=supreme%20small%20box%20tee%20pique','https://stockx.com/search?s=supreme%20small%20box%20tee%20shirt','https://stockx.com/search?s=supreme%20necklace%20tee','https://stockx.com/search?s=supreme%20scarface','https://stockx.com/search?s=supreme%20scarface%20split','https://stockx.com/search?s=supreme%20ftw%20tee%20shirt','https://stockx.com/search?s=supreme%20dollar','https://stockx.com/search?s=supreme%20undercover%20dolls','https://stockx.com/search?s=supreme%20arabic%206-panel','https://stockx.com/search?s=supreme%20arabic%20facemask','https://stockx.com/search?s=supreme%20arabic%20tee%20l/s','https://stockx.com/search?s=supreme%20arabic%20sweatshirt','https://stockx.com/search?s=supreme%20araki','https://stockx.com/search?s=supreme%20gonz%20crew','https://stockx.com/search?s=supreme%20gonz%20sweatshirt','https://stockx.com/search?s=supreme%20gonz%20butterfly%20tee%20shirt','https://stockx.com/search?s=supreme%20gonz%20tee%20shirt','https://stockx.com/search?s=supreme%20elephant%20tee%20shirt','https://stockx.com/search?s=supreme%20mike%20hill','https://stockx.com/search?s=supreme%20michael%20jackson','https://stockx.com/search?s=supreme%20nun','https://stockx.com/search?s=supreme%20nun','https://stockx.com/search?s=supreme%20anatomy','https://stockx.com/search?s=supreme%20akira%20syringe','https://stockx.com/search?s=supreme%20akira%20neo','https://stockx.com/search?s=supreme%20akira%20yamagata','https://stockx.com/search?s=supreme%20akira%20arm','https://stockx.com/search?s=supreme%20akira%20pill','https://stockx.com/search?s=supreme%20akira%20syringe','https://stockx.com/search?s=supreme%20sade','https://stockx.com/search?s=supreme%20betty%20tee%20shirt','https://stockx.com/search?s=supreme%20krs%20one%20shirt','https://stockx.com/search?s=supreme%20samurai','https://stockx.com/search?s=supreme%20neil%20%20tee%20shirt','https://stockx.com/search?s=supreme%20neil%20%20tee%20shirt','https://stockx.com/search?s=supreme%20neil%20%20tee%20shirt','https://stockx.com/search?s=supreme%20neil%20%20tee%20shirt','https://stockx.com/search?s=supreme%20neil%20%20tee%20shirt','https://stockx.com/search?s=supreme%20morissey%20tee%20shirt','https://stockx.com/search?s=supreme%20gucci%20mane%20tee%20shirt','https://stockx.com/search?s=supreme%20ali%20warhol','https://stockx.com/search?s=supreme%20sideline','https://stockx.com/search?s=prophere','https://stockx.com/search?s=supreme%20box%20logo%20crew','https://stockx.com/search?s=box%20logo%20sweatshirt','https://stockx.com/search?s=supreme%20box%20logo%20tee']
    searchlist = ['https://stockx.com/search?s=balenciaga','https://stockx.com/search?s=balenciaga']
    newlist = []
    oldlist = []
    # for url in alist:
    #     driver = webdriver.Chrome()
    #     driver.get(url)
    #     #time.sleep(5)
    #     htmlSource = driver.page_source
    #     driver.close()

    #     soup = BeautifulSoup(htmlSource,'html.parser')

    #     links = soup.find_all("a",{"class":"tile browse-tile"})

    #     for url in links:
    #         handles = url.get("href")
    #         newlist.append('https://stockx.com'+handles)
    #         print('https://stockx.com'+handles)


    for url in searchlist:
        driver = webdriver.Chrome()
        driver.get(url)
        htmlSource = driver.page_source
        driver.close()
        soup = BeautifulSoup(htmlSource,'html.parser')
        links = soup.find_all("div",{"class":"result-tile"})
        for url in links:
            handles = str(url).split()[2].split('"')[1]
            newlist.append('https://stockx.com/'+handles)
            print('https://stockx.com/'+handles)

    with open ('prodlist.csv','r') as fin:
        reader = csv.reader(fin)
        for line in reader:
            for entry in line:
                oldlist.append(entry)
    with open('instock.csv','r') as fin:
        reader = csv.reader(fin)
        for line in reader:
            oldlist.append(f"https://stockx.com/{line[0]}")
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
    return int(math.ceil(x / 10000.0)) * 10000


#Request all links.
async def fetch(url, session):
    try:
        async with session.get(url) as response:
            return await response.read()
    except:
        print(f"{datetime.now()}..... failed to get {url}")

async def run(r):
    tasks = []
    async with ClientSession() as session:
        num = 0
        for i in range(len(urllist)):
            task = asyncio.ensure_future(fetch(urllist[i], session))
            tasks.append(task)
            num+= 1
        print(f"{datetime.now()}..... Total task: {num}")
        responses = await asyncio.gather(*tasks)
        for entry in responses:
            soup = BeautifulSoup(entry, "html.parser")
            g_sku = soup.find_all("div",{"class":{"detail"}})
            if len(entry)>30000:
                htmllist.append(entry)
    percentage = (len(htmllist)*100)/num
    print(f"{datetime.now()}..... Total task working: {len(htmllist)}, %{percentage}")

        # you now have all response bodies in this variable

def format1():

    with open ('instock.json','r') as fin:
        jsondata = json.load(fin)
    #NEW
    with open("imagelibrary.json", 'w') as fout:
        jsondata2 = json.dumps(imgdict,indent = 4)
        json.dump(jsondata2,fout)

    for i in range(len(htmllist)):
        try:
            soup = BeautifulSoup(htmllist[i], "html.parser")
            g_check = soup.find_all("div", {"class": "stat-value stat-small"})
            g_name = soup.find("h1",{"class": "name"})
            print(f"{datetime.now()}..... Formatting data for {g_name.text}")
            g_data = soup.find_all("div", {"class": "market-summary"})
            for item in g_data:
                g_size = item.contents[0].find_all("div", {"class": "inset"})
            name = g_name.text.split()
            bogo =0
            if 'Box' and 'Supreme' in name:
                bogo = 1
            taginput = ','.join(name)
            handleinput = '-'.join(name).lower()
            g_sku = soup.find_all("div",{"class":{"detail"}})
            sku = str(g_sku[0].contents[1]).split()[1]
            lendictval = 0
            ready = 0
            try:
                readyjson = jsondata[handleinput]
                for entry in readyjson:
                    handlelist.append(handleinput)
                    sizelist.append(entry['size'])
                    pricelist.append(entry['price'])
                    variantqty.append(entry['quantity'])
                    lendictval+=1
                    if int(entry['quantity']) > 0:
                        ready = 1

            except:
                pass

            bodylist.append('<meta charset="utf-8"> <div class="title"> <meta charset="utf-8"> <div class="Trust__container__3bA3U" data-reactid="115"> <div class="Trust__image-container__3yIDD" data-reactid="116"><img src="https://www.goat.com/images/products/icon_verification@2x.png" width="30" height="30" class="Trust__image__3gb_e" data-reactid="117"></div> <div class="Trust__title__3cC5B" data-reactid="118"><strong>1000% AUTHENTIC</strong></div> <div class="Trust__desc__32B5p" data-reactid="119"> <p class="p1">Semua sneaker dari VTL melewati LEGIT CHECK oleh tim profesional untuk memastikan keaslian sneaker tersebut.</p> <p class="p1"> </p> </div> </div> <div class="Trust__container__3bA3U" data-reactid="120"> <div class="Trust__image-container__3yIDD" data-reactid="121"><img src="https://www.goat.com/images/products/icon_return@2x.png" width="30" height="30" class="Trust__image__3gb_e" data-reactid="122"></div> <div class="Trust__title__3cC5B" data-reactid="123"><strong>RETURNS</strong></div> <div class="Trust__desc__32B5p" data-reactid="124">Kami menerima pengembalian barang pada Brand New sneakers yang tetap dalam kondisi yang sama seperti yang dikirim. Kami akan memberikan <em>refund</em> untuk jumlah yang telah dibayar (di kurang biaya pengiriman) dalam bentuk <em>store credit</em>. Mohon hubungi kami untuk info lebih lanjut.</div> </div> </div>')
            vendorlist.append('Vendor')
            publishlist.append('TRUE')
            option1name.append('Size')
            giftcardlist.append('FALSE')
            imgposition = 1

            if type(imgdict[namekey[i]]) == list:
                for entry in imgdict[namekey[i]]:
                    imglist.append(entry)
                    imgpos.append(imgposition)
                    imgposition+=1
            else:
                imglist.append(imgdict[namekey[i]])
                imgpos.append(imgposition)

            titlelist.append(g_name.text)
            if ready > 0:
                taginput = ','.join(name)+','+sku.strip()+',ready'
            else:
                taginput = ','.join(name)+','+sku.strip()
            if bogo >0:
                taginput = taginput+',bogo'
            taglist.append(taginput)





        #Data list
            print(f"{datetime.now()}..... Formatting CSV file")
            if g_check[0].text != '$--':
                if g_size != []:
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
                            lendictval+=1
                            if int(price) > 500:
                                try:
                                    price = int(price)
                                    idr = (price+45)*1.08*13800 #format price + formula
                                    idr = roundup(idr)

                                except:
                                    idr = ""
                            elif int(price)>300:
                                try:
                                    price = int(price)
                                    idr = (price+45)*1.09*13800 #format price + formula
                                    idr = roundup(idr)

                                except:
                                    idr = ""
                            elif int(price)>200:
                                try:
                                    price = int(price)
                                    idr = (price+45)*1.1*13800 #format price + formula
                                    idr = roundup(idr)

                                except:
                                    idr = ""
                            elif int(price)>100:
                                try:
                                    price = int(price)
                                    idr = (price+45)*1.1*13800 #format price + formula
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
                            variantgrams.append('2000')
                            varianttrack.append('shopify')
                            variantqty.append('1')
                            variantpolicy.append('deny')
                            variantfull.append('manual')
                            variantreq.append('TRUE')
                            varianttax.append('FALSE')
                            variantweight.append('kg')
                else:
                    g_price = soup.find_all("div", {"class": "stat-value stat-small"})
                    price = int(g_price[0].text.replace('$',''))*13800*1.1
                    lendictval+=1
                    sizelist.append("(PO) One Size")
                    pricelist.append(price)
                    variantgrams.append('2000')
                    varianttrack.append('shopify')
                    variantqty.append('1')
                    variantpolicy.append('deny')
                    variantfull.append('manual')
                    variantreq.append('TRUE')
                    varianttax.append('FALSE')
                    variantweight.append('kg')
            else:
                print("HEREE")

            while len(imglist)>len(sizelist):
                sizelist.append('')
                variantgrams.append('')
                varianttrack.append('')
                variantqty.append('')
                variantpolicy.append('')
                variantfull.append('')
                variantreq.append('')
                varianttax.append('')
                variantweight.append('')
            while len(sizelist) > len(imglist):
                imglist.append('')
            while len(sizelist) > len(imgpos):
                imgpos.append('')

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
                variantgrams.append('2000')
            while len(sizelist)>len(varianttrack):
                varianttrack.append('shopify')
            while len(sizelist)>len(variantqty):
                variantqty.append('1')
            while len(sizelist)>len(variantpolicy):
                variantpolicy.append('deny')
            while len(sizelist)>len(variantfull):
                variantfull.append('manual')
            while len(sizelist)>len(variantreq):
                variantreq.append('TRUE')
            while len(sizelist)>len(varianttax):
                varianttax.append('FALSE')
            while len(sizelist)>len(variantweight):
                variantweight.append('kg')
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
            while len(sizelist) > len(taglist):
                taglist.append('')


            print(f"{datetime.now()}..... Total shoes in {g_name.text} is {lendictval}")
            lendict[g_name.text] = lendictval




        except:
            print(f"{datetime.now()}..... 'Failed to extract {urllist[i]}")

            with open('prodlistfail.txt','a') as fout:
                fout.write(urllist[i])
                fout.write('\n')









def export():
    finaldict = OrderedDict({'Handle': handlelist, 'Title': titlelist, 'Body (HTML)': bodylist, 'Vendor': vendorlist, 'Type': vendorlist, 'Tags': taglist, 'Published':publishlist, 'Option1 Name':option1name, 'Option1 Value':sizelist, 'Option2 Name':emptylist,'Option2 Value': emptylist, 'Option3 Name': emptylist, 'Option3 Value':emptylist,'Variant SKU': emptylist, 'Variant Grams': variantgrams, 'Variant Inventory Tracker': varianttrack, 'Variant Inventory Qty': variantqty, 'Variant Inventory Policy': variantpolicy, 'Variant Fullfilment Service':variantfull, 'Variant Price': pricelist, 'Variant Compare': emptylist, 'Variant Requires Shipping': variantreq, 'Variant Taxable': varianttax, 'Variant Barcode': emptylist, 'Image Src': imglist, 'Image Position': imgpos, 'Image Alt Text': emptylist, 'Gift Card': giftcardlist, 'SEO Title': emptylist, 'SEO Description': emptylist, 'Google Shopping / Google Product Category': emptylist,'Google Shopping / Gender':emptylist, 'Google Shopping / Age Group':emptylist,'Google Shopping / MPN':emptylist,'Google Shopping / AdWords Grouping':emptylist,'Google Shopping / AdWords Labels':emptylist,'Google Shopping / Condition':emptylist,'Google Shopping / Custom Product':emptylist,'Google Shopping / Custom Label 0':emptylist,'Google Shopping / Custom Label 1':emptylist,'Google Shopping / Custom Label 2':emptylist,'Google Shopping / Custom Label 3':emptylist,'Google Shopping / Custom Label 4':emptylist,'Variant Image':emptylist,'Variant Weight Unit':variantweight,'Variant Tax Code':emptylist})
    dlist = list(finaldict.values())
    print(f"{datetime.now()}..... Exporting")
    with open('export.csv','a',newline = '') as fout:
        writer = csv.writer(fout)
        count = 0
        for i in range(len(finaldict['Handle'])):
            exlist = []
            for entry in dlist:
                try:
                    exlist.append(entry[i])
                except:
                    print('FAIL' + str(type(entry)) + str(len(entry)))
            writer.writerow(exlist)


async def gets(url, session):
    async with session.get(url) as response:
        return await response.read()

async def fetchimg(r):
    for i in range(len(htmllist)):

        soup = BeautifulSoup(htmllist[i], "html.parser")
        g_sku = soup.find_all("div",{"class":{"detail"}})
        if g_sku == []:
            print(htmllist[i])
        sku = str(g_sku[0].contents[1]).split()[1]
        g_file = soup.find("div",{"class":{"full"}})
        g_name = soup.find("h1",{"class": "name"})
        namekey.append(g_name.text)
        g_link = soup.find("div",{"class":{'image-container'}})
        name = g_name.text
        if sku == 'TBD':
            url2 = f'https://www.stadiumgoods.com/search/go?w={("%20").join(g_name.text.split(" "))}'
            skulist.append(url2)
        else:
            sku.replace(' ','-')
            url2 = f'https://www.stadiumgoods.com/search/go?w={("%20").join(sku.split("-"))}'
            skulist.append(url2)
        sku.replace(' ','-')

        if g_link is not None:
            if len(str(g_file.contents).split('"')[5]) < 60:
                stockxdict[namekey[i]] = str(g_link.contents).split('"')[5]
            else:
                stockxdict[namekey[i]] =str(g_file.contents).split('"')[5]
        else:
            g_thumbs = soup.find("div",{"class":{"gallery-thumbs"}})
            if g_thumbs is not None:
                g_thumbs = soup.find("div",{"class":{"gallery-thumbs"}})
                stockxdict[namekey[i]] = []
                for entry in g_thumbs.contents:
                    stockxdict[namekey[i]].append(str(entry).split('"')[-2])
            else:
                g_link = soup.find("div",{"class":{'full'}})
                img = str(g_link.contents).split('"')[-2]
                if img != '':
                    stockxdict[namekey[i]] = str(g_link.contents).split('"')[-2]
                else:
                    stockxdict[namekey[i]] = 'http://nptel.ac.in/LocalChapter/Assets/college_logo/dummy_logo.png'
        print(f"printing stockx img urls{stockxdict[namekey[i]]}")
    for entry in stockxdict.keys():
        print(entry)
    print(f"{datetime.now()}..... Success made html list line 338")
    tasks = []
    async with ClientSession() as session:
        for i in range(len(skulist)):
            task = asyncio.ensure_future(gets(skulist[i], session))
            tasks.append(task)
        responses = await asyncio.gather(*tasks)
        for entry in responses:
            sghtml.append(entry)



        for i in range(len(responses)):

            print(f"{datetime.now()}..... Getting IMG URL from {skulist[i]}")
            soup2 = BeautifulSoup(sghtml[i],"html.parser")
            g_file = soup2.find_all("div",{"class":{"product-gallery-image"}})
            #print("Successfully parsed img url")
            # print(g_file)
            total = 0

            if g_file != []:
                imgdict[namekey[i]] = []
                for item in g_file:
                    g_img = item.contents
                    a = str(g_img[1]).split()
                    counter = 0
                    for j in a:
                        # print(a)
                        if j == 'itemprop="image"':
                            imgdict[namekey[i]].append(a[counter+1].split('"')[1])
                            total+=1
                        else:
                            counter+=1
            else:
                total=len(stockxdict[namekey[i]])
                imgdict[namekey[i]] =stockxdict[namekey[i]]
            print(f"{datetime.now()}..... Success extract {total} images line 378")
            print(stockxdict[namekey[i]])




            # print(total)
            # for count in range(total):
            #     try:
            #         #print(titlelist[count])
            #         if titlelist[count] == '':
            #             print('empty')
            #             # imglist.append('')
            #             # imgpos.append('')
            #         else:
            #             print('occupied')
            #     except:
            #         pass
        # while len(sizelist) > len(imglist):
        #     imglist.append('')
        # while len(sizelist) > len(imgpos):
        #     imgpos.append('')

    # finaldict['Image Src'] = imglist




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
    while True:
        print(f"{datetime.now()}..... Starting program")
        startTime = datetime.now()
        #geturl()
        with open('prodlist.csv','r') as fin:
            csvreader = csv.reader (fin,delimiter =',')
            for line in csvreader:
                for entry in line :
                    #print("Getting image URL")
                    if entry != '':
                        if entry not in urllist:
                            urllist.append(entry)
        urllist = sorted(urllist)
        for entry in urllist:
            print(entry)
        with open('export.csv','w',newline = '') as fout:
            writer = csv.writer(fout)
            writer.writerow(['Handle', 'Title', 'Body (HTML)', 'Vendor', 'Type', 'Tags', 'Published', 'Option1 Name', 'Option1 Value', 'Option2 Name', 'Option2 Value', 'Option3 Name', 'Option3 Value', 'Variant SKU', 'Variant Grams', 'Variant Inventory Tracker', 'Variant Inventory Qty', 'Variant Inventory Policy', 'Variant Fullfilment Service', 'Variant Price', 'Variant Compare', 'Variant Requires Shipping', 'Variant Taxable', 'Variant Barcode', 'Image Src', 'Image Position', 'Image Alt Text', 'Gift Card', 'SEO Title', 'SEO Description', 'Google Shopping / Google Product Category', 'Google Shopping / Gender', 'Google Shopping / Age Group', 'Google Shopping / MPN', 'Google Shopping / AdWords Grouping', 'Google Shopping / AdWords Labels', 'Google Shopping / Condition', 'Google Shopping / Custom Product', 'Google Shopping / Custom Label 0', 'Google Shopping / Custom Label 1', 'Google Shopping / Custom Label 2', 'Google Shopping / Custom Label 3', 'Google Shopping / Custom Label 4', 'Variant Image', 'Variant Weight Unit', 'Variant Tax Code'])

        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(run(len(urllist)))
        print(f"{datetime.now()}..... Getting Stockx data")
        loop.run_until_complete(future)
        print(f"{datetime.now()}.....Getting img urls")
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(fetchimg(len(htmllist)))
        loop.run_until_complete(future)
        format1()
        export()
        print("\007")
        print(f"Finished in {datetime.now() - startTime}")
        print(f"{datetime.now()}..... Done")
        time.sleep(21600)




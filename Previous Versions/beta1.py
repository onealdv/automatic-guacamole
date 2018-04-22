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

def webscraper():
    with open('export.csv','w') as fout:
                    writer = csv.writer(fout)
                    writer.writerow(['Handle', 'Title', 'Body (HTML)', 'Vendor', 'Type', 'Tags', 'Published', 'Option1 Name', 'Option1 Value', 'Option2 Name', 'Option2 Value', 'Option3 Name', 'Option3 Value', 'Variant SKU', 'Variant Grams', 'Variant Inventory Tracker', 'Variant Inventory Qty', 'Variant Inventory Policy', 'Variant Fullfilment Service', 'Variant Price', 'Variant Compare', 'Variant Requires Shipping', 'Variant Taxable', 'Variant Barcode', 'Image Src', 'Image Position', 'Image Alt Text', 'Gift Card', 'SEO Title', 'SEO Description', 'Google Shopping / Google Product Category', 'Google Shopping / Gender', 'Google Shopping / Age Group', 'Google Shopping / MPN', 'Google Shopping / AdWords Grouping', 'Google Shopping / AdWords Labels', 'Google Shopping / Condition', 'Google Shopping / Custom Product', 'Google Shopping / Custom Label 0', 'Google Shopping / Custom Label 1', 'Google Shopping / Custom Label 2', 'Google Shopping / Custom Label 3', 'Google Shopping / Custom Label 4', 'Variant Image', 'Variant Weight Unit', 'Variant Tax Code'])
    with open('prodlist.csv','r') as fin:
        csvreader = csv.reader (fin,delimiter =',')
        for line in csvreader:
            for entry in line :
                try:
                    print("Getting image URL")
                    url = 'https://stockx.com/'+entry
                    r = requests.get(url,stream = True)
                    print(f"Processing {url}")
                    soup = BeautifulSoup(r.content, "html.parser")
                    g_name = soup.find("h1",{"class": "name"})
                    g_data = soup.find_all("div", {"class": "market-summary"})
                    for item in g_data:
                        g_size = item.contents[0].find_all("div", {"class": "inset"})
                    name = g_name.text.split()
                    taginput = ','.join(name)
                    handleinput = url.split('/')[3]
                    imglist = []
                    imgpos = []
                    imgposition = 0




                    #get img url
                    print("Getting URL Data")
                    g_sku = soup.find_all("div",{"class":{"detail"}})
                    sku = str(g_sku[0].contents[1]).split()[1]
                    url2 = f'https://www.stadiumgoods.com/search/go?w={sku}'
                    print("Got SKU")
                    r2 = requests.get(url2, stream = True)
                    soup2 = BeautifulSoup(r2.content,"html.parser")
                    g_file = soup2.find_all("div",{"class":{"product-gallery-image"}})
                    print("Successfully parsed img url")
                    for item in g_file:
                        g_img = item.contents
                        a = str(g_img[1]).split()
                        counter = 0
                        for i in a:
                            if i == 'itemprop="image"':
                                 imglist.append(a[counter+1].split('"')[1])
                            else:
                                counter +=1
                    if imglist == []: #if not found in stadiumgoods
                        print("Getting stockx image")
                        # r = requests.get(url, stream = True)
                        # soup = BeautifulSoup(r.content,"html.parser")
                        g_file = soup.find("div",{"class":{"full"}})
                        imglist.append(str(g_file.contents).split('"')[5])



                    #Data list
                    handlelist = [handleinput]
                    sizelist = []
                    pricelist = []
                    emptylist = []
                    titlelist = [g_name.text]
                    bodylist = ['<meta charset="utf-8"> <div class="title"> <meta charset="utf-8"> <div class="Trust__container__3bA3U" data-reactid="115"> <div class="Trust__image-container__3yIDD" data-reactid="116"><img src="https://www.goat.com/images/products/icon_verification@2x.png" width="30" height="30" class="Trust__image__3gb_e" data-reactid="117"></div> <div class="Trust__title__3cC5B" data-reactid="118"><strong>1000% AUTHENTIC</strong></div> <div class="Trust__desc__32B5p" data-reactid="119"> <p class="p1">Semua sneaker dari VTL melewati LEGIT CHECK oleh tim profesional untuk memastikan keaslian sneaker tersebut.</p> <p class="p1"> </p> </div> </div> <div class="Trust__container__3bA3U" data-reactid="120"> <div class="Trust__image-container__3yIDD" data-reactid="121"><img src="https://www.goat.com/images/products/icon_return@2x.png" width="30" height="30" class="Trust__image__3gb_e" data-reactid="122"></div> <div class="Trust__title__3cC5B" data-reactid="123"><strong>RETURNS</strong></div> <div class="Trust__desc__32B5p" data-reactid="124">Kami menerima pengembalian barang pada Brand New sneakers yang tetap dalam kondisi yang sama seperti yang dikirim. Kami akan memberikan <em>refund</em> untuk jumlah yang telah dibayar (di kurang biaya pengiriman) dalam bentuk <em>store credit</em>. Mohon hubungi kami untuk info lebih lanjut.</div> </div> </div>']
                    vendorlist = ['Vendor']
                    taglist = [taginput]
                    publishlist = ['TRUE']
                    option1name = ['Size']
                    variantgrams = ['2000']
                    varianttrack = ['shopify']
                    variantqty = ['1']
                    variantpolicy = ['deny']
                    variantfull = ['manual']
                    variantreq = ['TRUE']
                    varianttax = ['FALSE']
                    variantweight = ['kg']
                    giftcardlist = ['FALSE']



                    #format csv file
                    print("Formatting CSV file")
                    for result in g_size:
                        size = result.contents[0].text
                        price = result.contents[1].text.replace('$','')
                        price = ''.join(price)

                        if price != 'Bid' and size != "All" and price != '' and size != '': #excludes empty price and "all" size entry
                            emptylist.append('') #adds entry in emptylist.
                            handlelist.append(handleinput)
                            titlelist.append('')
                            bodylist.append('')
                            vendorlist.append('')
                            taglist.append('')
                            publishlist.append('')
                            option1name.append('')
                            variantgrams.append('2000')
                            varianttrack.append('shopify')
                            variantqty.append('1')
                            variantpolicy.append('deny')
                            variantfull.append('manual')
                            variantreq.append('TRUE')
                            varianttax.append('FALSE')
                            variantweight.append('kg')
                            giftcardlist.append('')

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
                    sizelist.append('')
                    pricelist.append('')
                    emptylist.append('')
                    while len(sizelist) > len(imglist):
                        imglist.append('')
                    while len(sizelist) > len(imgpos):
                        imgpos.append('')
                    d = {'Handle': handlelist, 'Title': titlelist, 'Body (HTML)': bodylist, 'Vendor': vendorlist, 'Type': vendorlist, 'Tags': taglist, 'Published':publishlist, 'Option1 Name':option1name, 'Option1 Value':sizelist, 'Option2 Name':emptylist,'Option2 Value': emptylist, 'Option3 Name': emptylist, 'Option3 Value':emptylist,'Variant SKU': emptylist, 'Variant Grams': variantgrams, 'Variant Inventory Tracker': varianttrack, 'Variant Inventory Qty': variantqty, 'Variant Inventory Policy': variantpolicy, 'Variant Fullfilment Service':variantfull, 'Variant Price': pricelist, 'Variant Compare': emptylist, 'Variant Requires Shipping': variantreq, 'Variant Taxable': varianttax, 'Variant Barcode': emptylist, 'Image Src': imglist, 'Image Position': imgpos, 'Image Alt Text': emptylist, 'Gift Card': giftcardlist, 'SEO Title': emptylist, 'SEO Description': emptylist, 'Google Shopping / Google Product Category': emptylist,'Google Shopping / Gender':emptylist, 'Google Shopping / Age Group':emptylist,'Google Shopping / MPN':emptylist,'Google Shopping / AdWords Grouping':emptylist,'Google Shopping / AdWords Labels':emptylist,'Google Shopping / Condition':emptylist,'Google Shopping / Custom Product':emptylist,'Google Shopping / Custom Label 0':emptylist,'Google Shopping / Custom Label 1':emptylist,'Google Shopping / Custom Label 2':emptylist,'Google Shopping / Custom Label 3':emptylist,'Google Shopping / Custom Label 4':emptylist,'Variant Image':emptylist,'Variant Weight Unit':variantweight,'Variant Tax Code':emptylist}

                    dlist = list(d.values())
                    print("Exporting")
                    #print(dlist[0:2])
                    with open('export.csv','a') as fout:
                        writer = csv.writer(fout)
                        for i in range(len(d['Handle'])-1):
                            newlist = []
                            for entry in dlist:
                                newlist.append(entry[i])
                            writer.writerow(newlist)
                except:
                    print('Failed')

                    with open('prodlistfail.txt','w') as fout:
                        fout.write('https://stockx.com/'+entry)
            gc.collect()


def errorchecker():
    with open('prodlist.csv','r') as fin:
        csvreader = csv.reader (fin,delimiter =',')
        for line in csvreader:
            for entry in line :
                url = 'https://stockx.com/'+entry
                print(f"Processing {url}")
                resp = requests.get(url)
                print("Getting Error code")
                code = resp.status_code
                i = 1
                if code == 400:
                    print(f"Found {i} error links")
                    i+=1
                    with open('prodlistfail.txt','w') as fout:
                        fout.write('https://stockx.com/'+entry)
                gc.collect()



if __name__ == '__main__':
    print("Starting program")
    openfile('products_export.csv')
    webscraper()
    #errorchecker()
    print("Done")




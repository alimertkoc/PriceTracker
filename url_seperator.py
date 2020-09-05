from site_configs import *

URL_input = input("Type the URL:")
wantedPrice_input = input("Type the price you wanted to: ")

URLfile=open("urls.txt","a")
URLfile.write(URL_input+"\n" )

wantedPriceFile = open("wantedPrices.txt","a")
wantedPriceFile.write(wantedPrice_input+"\n")

URLfile.close()
wantedPriceFile.close()

URLfile = open("urls.txt","r")
urlArray = URLfile.readlines()

wantedPriceFile = open("wantedPrices.txt","r")
wantedPriceArray = wantedPriceFile.readlines()

URLfile.close()
wantedPriceFile.close()

def seperator(URL,wantedPrice):
    URL = URL.strip()
    wantedPrice = wantedPrice.strip()
    if URL.find('n11.com') != -1:
        n11_price_check(URL,wantedPrice)
    elif URL.find('gittigidiyor.com') != -1:
        gittigidiyor_price_check(URL,wantedPrice)
    elif URL.find('hepsiburada.com') != -1:
        hepsiburada_price_check(URL,wantedPrice)
    elif URL.find('epttavm.com') != -1:
        epttavm_price_check(URL,wantedPrice)
    elif URL.find('morhipo.com') != -1:
        morhipo_price_check(URL,wantedPrice)
    elif URL.find('amazon.com') != -1:
        amazon_price_check(URL,wantedPrice)
    elif URL.find('trendyol.com') != -1:
        trendyol_price_check(URL,wantedPrice)

for i in range(len(urlArray)):
    seperator(urlArray[i],wantedPriceArray[i])
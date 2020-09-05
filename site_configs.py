import requests
from bs4 import BeautifulSoup
import time
import smtplib
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

def n11_price_check(URL,wantedPrice):
    wantedPrice = int(wantedPrice)
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find("h1").get_text()
    price = soup.find("ins").get_text()
    price = price.replace(".", "")
    price = price.replace(",", ".")
    price = price[:-3]
    convertedPrice = float(price)
    timeText = time.asctime()
    print("Tarih: "+timeText)
    print("Ürün ismi: " + title.strip())
    print("Fiyat: "+str(convertedPrice)+"₺")
    if (convertedPrice < wantedPrice):
        send_email(URL)

def gittigidiyor_price_check(URL,wantedPrice):
    wantedPrice = int(wantedPrice)
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find("h1").get_text()
    price = soup.find(id="sp-price-lowPrice").get_text()
    price = price.strip()
    price = price.replace(".","")
    price = price.replace(",", ".")
    price = price[:-3]
    convertedPrice = float(price)
    timeText = time.asctime()
    print("Tarih: "+timeText)
    print("Ürün ismi: " + title.strip())
    print("Fiyat: "+str(convertedPrice)+"₺")
    if (convertedPrice < wantedPrice):
        send_email(URL)

def trendyol_price_check(URL,wantedPrice):
    wantedPrice = int(wantedPrice)
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    marka = soup.find("h1").get_text().strip()
    #title = soup.find('span', {'class' : 'pr-nm'}).get_text()
    price = soup.find('span', {'class' : 'prc-slg'}).get_text()
    price = price.strip()
    price = price.replace(",", ".")
    price = price[:-3]
    convertedPrice = float(price)
    timeText = time.asctime()
    print("Tarih: "+timeText)
    print("Ürün ismi: " + marka)
    print("Fiyat: "+str(convertedPrice)+"₺")
    if (convertedPrice < wantedPrice):
        send_email(URL)

def hepsiburada_price_check(URL,wantedPrice):
    wantedPrice = int(wantedPrice)
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    marka = soup.find("h1").get_text()
    #title = soup.find('span', {'class' : 'pr-nm'}).get_text()
    price = soup.find(id="offering-price").get_text()
    price = price.strip()
    price = price.replace(",", ".")
    price = price[:-3]
    convertedPrice = float(price)
    timeText = time.asctime()
    print("Tarih: "+timeText)
    print("Ürün ismi: " + marka)
    print("Fiyat: "+str(convertedPrice)+"₺")
    if (convertedPrice < wantedPrice):
        send_email(URL)

def epttavm_price_check(URL,wantedPrice):
    wantedPrice = int(wantedPrice)
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find("h1").get_text()
    price = soup.find('span', {'itemprop' : 'lowPrice'}).get_text()
    price = price.replace(",", ".")
    price = price[:-3]
    convertedPrice = float(price)
    timeText = time.asctime()
    print("Tarih: "+timeText)
    print("Ürün ismi: " + title.strip())
    print("Fiyat: "+str(convertedPrice)+"₺")
    if (convertedPrice < wantedPrice):
        send_email(URL)

def morhipo_price_check(URL,wantedPrice):
    wantedPrice = int(wantedPrice)
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find("h1").get_text()
    price = soup.find('span', {'class' : 'final-price'}).get_text()
    price = price.replace(",", ".")
    price = price[:-3]
    convertedPrice = float(price)
    timeText = time.asctime()
    print("Tarih: "+timeText)
    print("Ürün ismi: " + title.strip())
    print("Fiyat: "+str(convertedPrice)+"₺")
    if (convertedPrice < wantedPrice):
        send_email(URL)

def amazon_price_check(URL,wantedPrice):
    wantedPrice = int(wantedPrice)
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    price = price.replace(".", "")
    price = price.replace(",", ".")
    convertedPrice = float(price[1:])
    timeText = time.asctime()
    print("Tarih: "+timeText)
    print("Ürün ismi: " + title.strip())
    print("Fiyat: "+str(convertedPrice)+"₺")
    if (convertedPrice < wantedPrice):
        send_email(URL)

def send_email(URL):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('alimertkoc4@gmail.com','rhrqnuqmhqyplcsx')
    subject = 'Urun fiyati dustu!'
    body = 'PriceTracker uygulamasina kaydetmis oldugunuz urunun fiyati dustu. Linke goz atin.'
    urlmessage = URL

    msg = f"Subject: {subject}\n\n{body}\n\n{urlmessage}"

    server.sendmail(
        'alimertkoc4@gmail.com',
        'alimertkoc0@gmail.com',
        msg
    )
    print("E-Mail Yollandi.")
    server.quit()


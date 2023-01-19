from bs4 import BeautifulSoup

import requests


headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15'}

AmazonSearchBarUrl = 'https://www.amazon.in/s?k='
MintraSearchBarUrl = 'https://www.myntra.com/'
FlipkartSearchBarUrl = 'https://www.flipkart.com/search?q='

SearchThis = input("What do want to search : ")

PageAmazon = requests.get(AmazonSearchBarUrl+SearchThis, headers=headers).text
PageMintra = requests.get(MintraSearchBarUrl+SearchThis, headers= headers).text
pageFlipkart = requests.get(FlipkartSearchBarUrl+SearchThis, headers=headers).text


soupAmazon = BeautifulSoup(PageAmazon, 'lxml')
soupMintra = BeautifulSoup(PageMintra, 'lxml')
soupFlipkart = BeautifulSoup(pageFlipkart, 'lxml')

# Getting Link of particular product from main search page
outputAmazonMainDiv = soupAmazon.find('div',class_='s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_1')
outputAmazonProductInfo = outputAmazonMainDiv.find('div', class_="a-section")
AmazonProduct = outputAmazonProductInfo.find('a', class_='a-link-normal s-no-outline')

AmazonProductName = outputAmazonMainDiv.find('h2').text
AmazonProductPrice = outputAmazonMainDiv.find('span', class_= 'a-price').find('span').text
AmazonProductLink ='https://www.amazon.in/' + AmazonProduct['href']

print(AmazonProductName)
print(AmazonProductPrice)
print(AmazonProductLink)

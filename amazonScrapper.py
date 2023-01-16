from bs4 import BeautifulSoup

import requests


headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15'}

AmazonSearchBarUrl = 'https://www.amazon.in/s?k='

SearchThis = input("What do want to search : ")

mainPage = requests.get(AmazonSearchBarUrl+SearchThis, headers=headers).text

soup = BeautifulSoup(mainPage, 'lxml')

output = soup.find('div',class_='sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 AdHolder sg-col s-widget-spacing-small sg-col-4-of-20')

output_brand = output.find('span',class_='a-size-base-plus a-color-base').text
output_price = output.find('span', class_='a-price-whole').text
output_productName = output.find('span', class_='a-size-base-plus a-color-base a-text-normal').text


print('Product : ',output_productName)
print('Brand Name : ',output_brand)
print('Price : ',output_price)
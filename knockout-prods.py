'''
Simple script to scrap list of products from knockout.com.bd 
and saving the scrapped data to a csv file.
[PUN]: onekdin por scrapping korte mon chaise tai kortesi; xD
'''


import requests
from bs4 import BeautifulSoup
import csv


target_url = 'https://knock.com.bd/shop/page/'

with open('knock-out-output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    # write the column-header in the first row
    writer.writerow(['Category', 'Product', 'Price'])
    # page counts
    count = 1
    while True:
        # make request to the url
        response = requests.get(target_url + str(count))

        if response.status_code == 200:

            # get the soup of the html content.
            soup = BeautifulSoup(response.content, 'html.parser')

            # create new .csv file to store the data

            #get desired data by inspecting html tags
            print('Category |  Product Title               | Unit Price(BDT)')
            # print('_______________________________________________________')
            for ele in soup.find_all('div', class_='box'):
                title = ele.select_one('div.box-text-products > div.title-wrapper')
                
                try:
                    price = ele.select_one('bdi').text.strip()
                except:
                    price = 'N/A'

                try:
                    prod_cat = title.select_one('p.product-cat').text.strip()
                except:
                    prod_cat = 'N/A'

                try:
                    prod_title = title.select_one('p.product-title> a').text.strip()
                except:
                    prod_title = 'N/A'
                
                print(f'{count} => {prod_title}')

                # write row data in csv
                writer.writerow([prod_cat, prod_title, price])
        else:
            break
        count += 1





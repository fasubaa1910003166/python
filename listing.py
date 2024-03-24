# i want to check new listing in fb marketpalce listing with this link: https://www.facebook.com/marketplace/sunshinecoast/search/?query=iphone and if there will be any
#new listiuings then i want to send an email to myself with the link of the new listing.
# i will run this script every 1 hour to check for new listings
import csv
import random

import requests
from selenium import webdriver
import smtplib
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent

all_listing_links = []

ua = UserAgent()
user_agent = ua.random

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'user-agent={user_agent}')

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()


csv_file = "products_link.csv"
def products_links_csv():
    header = ["product_links"]

    with open(csv_file, 'a+', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)

        # Write header
        if file.tell() == 0:  # Check if file is empty
            writer.writerow(header)

        writer.writerow(["https://www.facebook.com/marketplace/sunshinecoast/search?daysSinceListed=1&query=iphone&exact=false"])

products_links_csv()

time.sleep(3)
def get_prices_from_csv(csv_file):
    prices = []  # Initialize an empty list to store prices
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header if present
        for row in reader:
            # Assuming price is in the first column (index 0)
            price = row[0].strip()  # Remove any leading/trailing spaces
            prices.append(price)
    return prices

def getting_theall_links():
    driver.get("https://www.facebook.com/marketplace/sunshinecoast/search?daysSinceListed=1&query=iphone&exact=false")
    time.sleep(15)

    all_listing_linkss = driver.find_elements(By.XPATH, '//div[@aria-label="Collection of Marketplace items"]//a')
    for all in all_listing_linkss:
        link_of_product = all.get_attribute('href')
        print(link_of_product)
        all_listing_links.append(link_of_product)

getting_theall_links()
# checking after 5 - 10 minuites if there will be any new item then i will scrape it

checking = 1

def checking_for_new_listing():
    global checking  # Declare 'checking' as global
    while True:
        print(f"{checking} Checking for new listing")
        driver.get("https://www.facebook.com/marketplace/sunshinecoast/search?daysSinceListed=1&query=iphone&exact=false")
        time.sleep(random.randint(15, 25))
        all_listing_linkss = driver.find_elements(By.XPATH, '//div[@aria-label="Collection of Marketplace items"]//a')
        price_ofproduct = driver.find_elements(By.XPATH, '//div[@aria-label="Collection of Marketplace items"]//a//span[@class="x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x676frb x1lkfr7t x1lbecb7 x1s688f xzsf02u"]')
        title_of_product = driver.find_elements(By.XPATH, '//div[@class="x1gslohp xkh6y0r"][2]//span[@class="x1lliihq x6ikm8r x10wlt62 x1n2onr6"]')
        location_of_product = driver.find_elements(By.XPATH, '//div[@class="x1gslohp xkh6y0r"][3]//span[@class="x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft x1j85h84"]')
        csv_file_path = csv_file  # Replace 'your_file.csv' with the path to your CSV file
        prices_list = get_prices_from_csv(csv_file_path)
        print(prices_list)

        for listing, pro_price, title, locat in zip(all_listing_linkss, price_ofproduct, title_of_product, location_of_product):
            link_of_product = listing.get_attribute('href')
            if link_of_product not in all_listing_links and link_of_product not in prices_list:
                price_ofthis_product = pro_price.text
                product_title = title.text
                product_location = locat.text
                print("New listing found: ", link_of_product)

                all_listing_links.append(link_of_product)
                with open(csv_file, 'a+', encoding='utf-8', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([link_of_product])
                print(f'New Listing Found: Product Link: {link_of_product} - {product_title} - {price_ofthis_product} - {product_location}')
            else:
                print("No new listing found")

        checking += 1

checking_for_new_listing()



# Call the function to execute the code



time.sleep(555)



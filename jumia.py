import requests
from bs4 import BeautifulSoup
import csv
def scrape_jumia_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    products = []
    count = 0
    # Find all items
    main_dt = soup.find_all('div', class_="itm col")
    for item in main_dt:
        # Find product name and price elements for each item
        name_element = item.find('div', class_="name")
        price_element = item.find('div', class_="prc")
        if name_element and price_element:
            count += 1
            product_name = name_element.get_text(strip=True)
            product_price = price_element.get_text(strip=True)
            products.append([product_name, product_price])
    return count, products
def write_to_csv(data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Product Name', 'Price'])
        for product in data:
            writer.writerow(product)
#  Jumia
jumia_url = "https://www.jumia.co.ke/"
# Scrape data from the website
count, products = scrape_jumia_data(jumia_url)
# Write the scraped data to a CSV file
write_to_csv(products, 'jumia.csv')
print(f"Scraped {count} products.")
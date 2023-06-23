# Python Code: scrape_and_manage.py
import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

# Scraping data from a website
url = 'https://example.com/products'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extracting relevant data from the webpage
products = soup.find_all('div', class_='product')
data = []

for product in products:
    name = product.find('h2').text
    price = product.find('span', class_='price').text
    description = product.find('p', class_='description').text

    # Creating a dictionary to store the extracted data
    product_data = {
        'name': name,
        'price': price,
        'description': description
    }

    data.append(product_data)

# Generating an XML file and storing the scraped data
root = ET.Element('products')

for product_data in data:
    product = ET.SubElement(root, 'product')

    name = ET.SubElement(product, 'name')
    name.text = product_data['name']

    price = ET.SubElement(product, 'price')
    price.text = product_data['price']

    description = ET.SubElement(product, 'description')
    description.text = product_data['description']

tree = ET.ElementTree(root)
tree.write('products.xml')

print("Scraping and XML file generation complete.")

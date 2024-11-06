from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import json
from urllib.parse import urljoin


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


url = "https://www.pascalcoste-shopping.com/esthetique/fond-de-teint.html"
driver.get(url)

time.sleep(5)  
page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")
product_list = soup.find_all("div", class_="uk-panel uk-position-relative")
products = []

for product in product_list:
    product_url = product.find("a", class_="product-item-link")["href"] if product.find("a", class_="product-item-link") else None
    name = product.find("h3", class_="product-name").text.strip() if product.find("h3", class_="product-name") else None
    brand = product.find("div", class_="uk-width-expand uk-first-column").text.strip() if product.find("div", class_="uk-width-expand uk-first-column") else None

    image_url = product.find("img", class_="product-image-photo")["src"] if product.find("img", class_="product-image-photo") else None


    if image_url and not image_url.startswith('http'):
     image_url = urljoin(url, image_url) 


    price = product.find("span", class_="uk-price").text.strip() if product.find("span", class_="uk-price") else None
    

    if name and price and image_url:
        products.append({
            "name": name,
            "price": price,
            "brand": brand,
            "imageUrl": image_url,
            "productUrl": product_url
        })


if products:
    with open('products.json', 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=4)
    print("Scraping completed. Data saved to 'products.json'.")
else:
    print("No products extracted.")


driver.quit()

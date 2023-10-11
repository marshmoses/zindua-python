import requests
from bs4 import BeautifulSoup
import csv

def scrape_jumia_products(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None
    soup = BeautifulSoup(response.text, 'html.parser')
    
    #deals of the week
    product_containers = soup.find_all("div", class_="product")
    product_data = []
    
    for product in product_containers:
        product_name = product.find('h3', class_='title').text
        brand_name = product.find('span', class_='brand').text
        price = product.find('div', class_='price').text
        discount = product.find("div", class_="discount").text
        num_reviews = product.find("div", class_="num-reviews").text
        product_rating = product.find("div", class_="rating-stars")["style"]
        product_rating = float(product_rating.split(':')[-1].split('%')[0]) / 20
        
        product_data.append([product_name, brand_name, price, discount, num_reviews, product_rating])
    
    return product_data
if __name__ == "__main__":
    jumia_url = "https://www.jumia.co.ke/deals-you-cant-miss/"
    product_data = scrape_jumia_products(jumia_url)
    
    if product_data:
        with open("jumia_products.csv", "w", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["Product Name", "Brand Name", "Price (Ksh)", 
            "Discount (%)", "Total Number of Reviews"
            , "Product Rating"])
            csv_writer.writerows(product_data)

import requests
from bs4 import BeautifulSoup
titles = [ ]
prices = [ ]
base_url = "https://books.toscrape.com/catalogue/page-{}.html"
for page in range (1, 51) : 
    url = base_url.format(page)
    print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    for book in books :
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        price = price.replace("Â£", "")
        price = price.strip()
        print(repr(price))
        price = float(price)
        if 20 <= price <= 40 : 
            print(price)
            titles.append(title)
            prices.append(price)    
import pandas as pd
df = pd.DataFrame ({
    "title" : titles,
    "price" : prices
})
print(df)
df.to_csv("bookstoscrape1.csv", index=False)
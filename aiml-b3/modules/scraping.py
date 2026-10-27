import requests
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/130.0.0.0 Safari/537.36"
    )
}

response = requests.get(
    url,
    headers=headers,
    timeout=15
)

print("Status code:", response.status_code)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Inspect the returned HTML to identify product containers
    products = soup.select("div[data-id]")
    print(products)
    for product in products:
        name = product.select_one("div.RG5Slk")
        price = product.select_one("div.hZ3P6w")
        rating = product.select_one("div.MKiFS6")
        link = product.select_one("a[href]")

        print("Product:", name.get_text(strip=True) if name else "N/A")
        print("Price:", price.get_text(strip=True) if price else "N/A")
        print("Rating:", rating.get_text(strip=True) if rating else "N/A")

        if link:
            print("Link:", "https://www.flipkart.com" + link["href"])

        print("-" * 50)
else:
    print("Request failed or access was restricted.")

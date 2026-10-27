import requests
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=fcb89a60-2219-4d7b-af63-fb3ef242e8f2&as-backfill=on"

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
    c = 1
    for product in products:
        name = product.select_one("div.RG5Slk")
        price = product.select_one("div.hZ3P6w")
        rating = product.select_one("div.MKiFS6")
        link = product.select_one("a[href]")
        print("Product Count : ",c)
        print("Product:", name.get_text(strip=True) if name else "N/A")
        print("Price:", price.get_text(strip=True) if price else "N/A")
        print("Rating:", rating.get_text(strip=True) if rating else "N/A")
        c+=1
        if link:
            print("Link:", "https://www.flipkart.com" + link["href"])

        print("-" * 50)
else:
    print("Request failed or access was restricted.")

import requests
from bs4 import BeautifulSoup
import csv

def fetch_page(url: str) -> str | None:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Encoding": "identity",
        "Connection": "close",
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text

    except requests.exceptions.RequestException as err:
        print(f"Connection failed: {err}")
        return None


def extraction_data(html_content: str) -> list[dict]:
    products_data = []
    soup = BeautifulSoup(html_content, "html.parser")
    cards = soup.find_all("article", class_="product_pod")

    for card in cards:
        a_tag = card.find("h3").find("a") 
        title = a_tag.get("title", "").strip()
        
        price_tag = card.find("p", class_="price_color")
        price = price_tag.get_text(strip=True)

        products_data.append({
            "title": title,
            "price": price,
        })

    return products_data

def save_data(data: list[dict]) -> list[dict]:
    fieldnames = ["title", "price"]

    with open("products.csv", mode="w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)  

    print("The file was successfully created.")
    return data

if __name__ == "__main__":
    target_url = "https://books.toscrape.com/index.html"
    html = fetch_page(target_url)

    if html:
        data = extraction_data(html)
        save_data(data)
    else:
        print("Some things went wrong")
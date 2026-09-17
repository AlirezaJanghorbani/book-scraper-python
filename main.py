import requests

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
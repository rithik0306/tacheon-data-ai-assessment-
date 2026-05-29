```python
import requests
import logging

logging.basicConfig(level=logging.INFO)

API_URL = "https://api.coingecko.com/api/v3/coins/markets"

PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1
}

def fetch_crypto_data():
    try:
        logging.info("Fetching data from CoinGecko API...")

        response = requests.get(API_URL, params=PARAMS)

        response.raise_for_status()

        data = response.json()

        logging.info("Data fetched successfully.")

        return data

    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
        return None


if __name__ == "__main__":
    fetch_crypto_data()
```

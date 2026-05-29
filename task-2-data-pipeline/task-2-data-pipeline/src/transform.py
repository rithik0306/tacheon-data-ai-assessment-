```python id="vxqbz9"
import pandas as pd


def transform_data(data):

    df = pd.DataFrame(data)

    required_columns = [
        "id",
        "symbol",
        "name",
        "current_price",
        "market_cap",
        "total_volume",
        "price_change_percentage_24h"
    ]

    df = df[required_columns]

    df = df.fillna(0)

    def price_category(change):
        if change > 5:
            return "Bullish"
        elif change < -5:
            return "Bearish"
        else:
            return "Stable"

    df["market_status"] = df["price_change_percentage_24h"].apply(price_category)

    return df
```

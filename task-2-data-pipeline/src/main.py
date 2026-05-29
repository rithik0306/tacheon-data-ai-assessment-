from fetch_data import fetch_crypto_data
from transform import transform_data

data = fetch_crypto_data()

if data:
    df = transform_data(data)

    print(df.head())
    print("Pipeline executed successfully.")

else:
    print("Failed to fetch data.")

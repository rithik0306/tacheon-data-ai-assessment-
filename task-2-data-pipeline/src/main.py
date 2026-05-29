from fetch_data import fetch_crypto_data
from transform import transform_data
from load_bigquery import load_to_bigquery

def main():

    data = fetch_crypto_data()

    if data:

        df = transform_data(data)

        print(df.head())

        # Uncomment when running locally with BigQuery credentials configured
        # load_to_bigquery(df)

        print("Pipeline executed successfully.")

    else:

        print("Failed to fetch data.")


if __name__ == "__main__":
    main()

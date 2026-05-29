from google.cloud import bigquery

def load_to_bigquery(df):

    client = bigquery.Client()

    table_id = "crypto-market-pipeline-497808.crypto_data.crypto_market_data"

    job = client.load_table_from_dataframe(
        df,
        table_id
    )

    job.result()

    print("Data loaded successfully into BigQuery.")

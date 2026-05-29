# Task 2 - Data Pipeline

## Overview

This task demonstrates a simple data pipeline that fetches cryptocurrency market data from the CoinGecko API, transforms the data, and prepares it for loading into Google BigQuery.


## API Chosen

**CoinGecko API**

Endpoint used:
https://api.coingecko.com/api/v3/coins/markets

### Why CoinGecko?

* Free to use
* No authentication required
* Provides structured JSON responses
* Suitable for demonstrating ETL concepts
* Contains real-world market data


## Pipeline Architecture

CoinGecko API

↓

fetch_data.py

↓

transform.py

↓

Google BigQuery

↓

SQL Analysis


## Components

### fetch_data.py

Responsible for:

* Calling the CoinGecko API
* Handling API failures
* Logging request status
* Returning JSON data

### transform.py

Responsible for:

* Converting JSON into a DataFrame
* Selecting required columns
* Handling missing values
* Creating derived analytical fields

### Derived Field

market_status

Logic:

* Bullish → Price change > 5%
* Stable → Price change between -5% and 5%
* Bearish → Price change < -5%

### load_bigquery.py

Responsible for:

* Connecting to BigQuery
* Loading transformed data into the destination table

### analysis.sql

Provides analytical insights using SQL queries.

## BigQuery Configuration

Project ID:
crypto-market-pipeline-497808

Dataset:
crypto_data

Table:
crypto_market_data


## SQL Analysis

Example analysis:

* Count cryptocurrencies by market status
* Calculate average price by category
* Compare bullish and bearish assets


## Production Considerations

### Scheduling

The pipeline can be scheduled using:

* Google Cloud Scheduler
* Apache Airflow
* Cron Jobs

### Monitoring

* Logging
* Retry mechanisms
* Failure alerts

### Scalability

* Partitioned BigQuery tables
* Incremental data loading
* Batch processing

## Conclusion

This solution demonstrates a simple but scalable ETL pipeline that collects market data, performs transformations, stores data in BigQuery, and enables analytical reporting through SQL.

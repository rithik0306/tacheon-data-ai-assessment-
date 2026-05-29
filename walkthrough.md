# Assessment Walkthrough

## Overview

This submission contains two tasks:

1. Product Scoping
2. Data Pipeline Development


## Task 1: Product Scoping

The goal was to design a solution that helps marketing teams quickly understand campaign performance across channels.

### My Approach

I focused on creating a simple MVP rather than a complex platform.

The proposed solution is a centralized Marketing Performance Intelligence Dashboard that consolidates campaign metrics from multiple marketing platforms.

### Key Decisions

* Prioritized internal analysts and marketing managers as primary users.
* Focused on cross-channel visibility and reporting consistency.
* Excluded advanced features such as AI chatbots, forecasting, and automated budget allocation from V1.

### What I Would Improve

With more time, I would explore:

* AI-generated recommendations
* Automated anomaly detection
* Client-facing dashboards


## Task 2: Data Pipeline

For the pipeline task, I selected the CoinGecko API.

### Why CoinGecko?

* Free to use
* No API key required
* Provides structured JSON data
* Easy to demonstrate ETL concepts

### Pipeline Flow

CoinGecko API

↓

Data Fetching

↓

Transformation

↓

BigQuery

↓

SQL Analysis

### Transformations Applied

* Selected relevant fields
* Handled missing values
* Added a derived field called `market_status`

### BigQuery

The transformed data is prepared for loading into BigQuery using a dedicated loading module.

### Production Considerations

If this were deployed in production, I would:

* Schedule runs using Cloud Scheduler or Airflow
* Add monitoring and alerting
* Use partitioned tables
* Implement incremental data loading

## Conclusion

This assessment focuses on building practical and maintainable solutions. My approach was to prioritize clarity, scalability, and simplicity while ensuring the solution meets the stated requirements.

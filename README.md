# Product Scraper Project

A modular Python web scraping project that extracts product data from a multi-page e-commerce site.

## Features

- Scrapes all products across multiple categories
- Handles pagination automatically
- Extracts:
  - Product name
  - Price
  - Rating
  - Description
  - Reviews count
  - Category
  - Product URL
  - Image URL
- Retry logic for failed requests
- Logging system
- CSV export
- Summary report generation

## Project Structure

- scraper.py → scraping logic
- utils/retry.py → retry handling
- utils/logger.py → logging system
- config.py → site configuration
- report.py → report generator
- main.py → project entry point

## Installation

- pip install -r requirements.txt
- python main.py

Outputs:

* output/products.csv
* output/process.log
* output/report.csv

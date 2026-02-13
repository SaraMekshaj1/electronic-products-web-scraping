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

## Website
<img width="1911" height="985" alt="image" src="https://github.com/user-attachments/assets/6716e17d-7a54-4941-a6be-663870211962" />

## Output
<img width="1919" height="845" alt="image" src="https://github.com/user-attachments/assets/9bca40f7-8a37-45e5-8b25-e727e47aa080" />



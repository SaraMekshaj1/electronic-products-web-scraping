import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from config import BASE_URL, HEADERS, CATEGORIES
from utils.retry import get_with_retry
from utils.logger import setup_logger


logger=setup_logger()
session=requests.Session()
session.headers.update(HEADERS)

def scrape_all_categories():
    all_data = []

    for category_name, category_path in CATEGORIES.items():
        msg=f"Scraping {category_name}..."
        logger.info(msg)
        category_products = scrape_category(category_name, category_path)
        all_data.extend(category_products)

    return all_data

def scrape_category(category_name, category_path):
    all_data=[]
    page=1
    fail_count=0
    MAX_FAILS=5
    total_start= time.time()
    total_products_sum=0

    while True:
        page_start= time.time()
        url= f"{urljoin(BASE_URL, category_path)}?page={page}"
        response=get_with_retry(session, url)
        
        if not response:
            fail_count+=1
            logger.warning(f"Skipping page {page} (request failed)")
            if fail_count>=MAX_FAILS:
                logger.info("Stopping: too many consecutive failures (end of pagination)")
                break
            page+=1
            continue
        if response.status_code == 404:
            break

        soup=BeautifulSoup(response.text, "lxml")
        products= soup.select("div.col-md-4")

        if not products:
            logger.info("No products found. End research")
            break

        for product in products:

            name_tag=product.select_one("a.title")
            name=name_tag.text.strip() if name_tag else None

            price_tag=product.select_one("h4.price")
            price=price_tag.text.strip() if price_tag else None

            description_tag=product.select_one("p.description")
            description=description_tag.text.strip() if description_tag else None

            rating = product.select_one("p[data-rating]")["data-rating"]

            product_url_tag=product.select_one("h4 a.title")
            product_url_src=product_url_tag["href"]
            product_url =urljoin(BASE_URL,product_url_src )

            reviews_tag=product.select_one("p.review-count span")
            reviews= reviews_tag.text.strip() if reviews_tag else None

            image_tag=product.select_one("img[itemprop='image']")
            image_src=image_tag["src"] if image_tag else None
            image_url=urljoin(BASE_URL,image_src)
    
            all_data.append({
                "product_name":name,
                "price":price,
                "description":description,
                "product_url":product_url,
                "rating":rating,
                "reviews_nr":reviews,
                "category":category_name, 
                "image_url":image_url
            })

        page_time= time.time()-page_start
        msg=f" Page {page} | {len(products)} {category_name} | {page_time:.2f}s"
        logger.info(msg)
        print(msg)

        page+=1
        time.sleep(0.2)

    total_products_sum+=len(all_data)
    total_time = time.time() - total_start
    logger.info(f"\n Total products: {len(all_data)}")
    logger.info(f"\n Total time{total_time:.2f}s")
  
    
    return all_data


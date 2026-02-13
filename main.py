import pandas as pd
import os
from scraper import scrape_all_categories
from report import generate_report

def main():
    print("Products Scraper Project Started")
    os.makedirs("output",exist_ok=True)

    data=scrape_all_categories()

    if data:
        df = pd.DataFrame(data)
        df.to_csv("output/products.csv", index=False)
        print("Data saved successfully!")

        generate_report("output/products.csv")  
        print("Report generated!")

    else:
        print("No data scraped.")



if __name__=="__main__":
    main()
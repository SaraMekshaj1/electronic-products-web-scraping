import pandas as pd
import os

def generate_report(csv_path="output/products.csv"):
    if not os.path.exists(csv_path) or os.path.getsize(csv_path) == 0:
        print("Report skipped: CSV is empty")
        return None
    
    df = pd.read_csv(csv_path)
    
    if df.empty:
        print("Report skipped: no data scraped")
        return None

    total_products = len(df)
    missing_categories = df["category"].isnull().sum()
    missing_prices = df["price"].isnull().sum()

    report = {
        "total_products_scraped": total_products,
        "missing_categories": missing_categories,
        "missing_prices": missing_prices
        
    }

    report_df = pd.DataFrame([report])
    report_df.to_csv("output/report.csv", index=False)

    return report

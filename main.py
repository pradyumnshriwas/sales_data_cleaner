import csv
import json

USD_TO_INR = 83

def clean_price(price):
    price = price.replace("$", "").replace('"', "").strip()
    return float(price)

def main():
    cleaned_data = []
    seen = set()

    with open("sales.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            order_id = int(row[0].strip())
            product = row[1].replace('"', '').strip()
            price_usd = clean_price(row[2])
            country = row[3].strip()

            key = (product, price_usd)
            if key in seen:
                continue
            seen.add(key)

            price_inr = round(price_usd * USD_TO_INR, 2)

            cleaned_data.append({
                "order_id": order_id,
                "product": product,
                "price_usd": price_usd,
                "price_inr": price_inr,
                "country": country
            })

    with open("clean_sales.json", "w") as json_file:
        json.dump(cleaned_data, json_file, indent=4)

    print("Cleaned data saved successfully!")

if __name__ == "__main__":
    main()

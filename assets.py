"""
Randomizing data
"""
from datetime import date
import datetime
import random
import csv
from faker import Faker


def create_csv(data, filename, fieldnames):
    """ 
    creating csv file
    """
    with open(filename, "w", encoding="utf-8") as f:
        csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
        csv_writer.writeheader()
        for row in data:
            csv_writer.writerow(row)


def create_assets(p):
    """
    generating random data for assets
    """
    fake = Faker()
    today_date = date.today()
    x = datetime.date(2022, 1, 1)
    asset_id = 1
    assets = []
    for _ in range(p):
        random_date = fake.date_between(x, today_date)
        assets.append({"id": asset_id, "purchase_date": random_date})
        asset_id += 1

    fieldnames = ["id", "purchase_date"]
    create_csv(assets, "assets.csv", fieldnames)

    return assets


def create_rentals(assets, q):
    """
    generating random data for rental
    """
    rental_id = 1
    rentals = []
    today_date = date.today()
    fake = Faker()
    for _ in range(q):
        asset = random.choice(assets)
        asset_date = asset["purchase_date"] + datetime.timedelta(days=1)
        is_asset = []
        for data in rentals:
            if data["asset_id"] == asset["id"]:
                is_asset.append(data["end_date"])
        if is_asset:
            asset_date = max(is_asset) + datetime.timedelta(days=1)
        asset_id = asset["id"]
        start_date = fake.date_between(asset_date, today_date)
        end_date = fake.date_between(start_date, today_date)
        rentals.append(
            {
                "id": rental_id,
                "asset_id": asset_id,
                "start_date": start_date,
                "end_date": end_date,
            }
        )
        rental_id += 1

    fieldnames = ["id", "asset_id", "start_date", "end_date"]
    create_csv(rentals, "rental.csv", fieldnames)
    return rentals


if __name__ == "__main__":
    random_assets = create_assets(10)
    create_rentals(random_assets, 20)

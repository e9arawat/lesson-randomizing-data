"""
Randomizing data
"""
from datetime import date
import datetime
import random
import csv


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
    today_date = date.today()
    assets = []
    for asset_id in range(1, p + 1):
        random_date = today_date - datetime.timedelta(days=random.randint(0, 500))
        assets.append({"id": asset_id, "purchase_date": random_date})

    fieldnames = ["id", "purchase_date"]
    create_csv(assets, "assets.csv", fieldnames)

    return assets


def create_rentals(assets, q):
    """
    generating random data for rental
    """
    rentals = []
    assets_copy = assets.copy()
    today_date = date.today()
    for rental_id in range(1, q + 1):
        if not assets_copy:
            print("No assets to rent")
            return None
        asset = random.choice(assets_copy)
        asset_date = asset["purchase_date"]
        end_dates = [
            data["end_date"] for data in rentals if data["asset_id"] == asset["id"]
        ]
        if end_dates:
            asset_date = max(end_dates) + datetime.timedelta(days=1)

        start_date = (
            date.today()
            if asset_date == today_date
            else today_date
            - datetime.timedelta(days=random.randint(1, (today_date - asset_date).days))
        )
        end_date = start_date + datetime.timedelta(days=random.randint(10, 100))
        if end_date >= today_date:
            assets_copy.remove(asset)

        rentals.append(
            {
                "id": rental_id,
                "asset_id": asset["id"],
                "start_date": start_date,
                "end_date": end_date,
            }
        )

    fieldnames = ["id", "asset_id", "start_date", "end_date"]
    create_csv(rentals, "rental.csv", fieldnames)
    return rentals


if __name__ == "__main__":
    random_assets = create_assets(10)
    create_rentals(random_assets, 20)

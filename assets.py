"""
Randomizing data
"""
from datetime import date, timedelta
import random

def create_assets(p):
    """
    generating random data for assets
    """
    today_date = date.today()
    assets = []
    for asset_id in range(1, p + 1):
        random_date = today_date - timedelta(days=random.randint(1, 500))
        assets.append({"id": asset_id, "purchase_date": random_date})
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
            break
        asset = random.choice(assets_copy)
        asset_date = asset["purchase_date"]
        end_dates = [
            data["end_date"] for data in rentals if data["asset_id"] == asset["id"]
        ]
        if end_dates:
            asset_date = max(end_dates) + timedelta(days=1)

        start_date = asset_date + timedelta(days=random.randint(0, 50))
        end_date = start_date + timedelta(days=random.randint(10, 100))
        if end_date >= today_date:
            assets_copy.remove(asset)

        rentals.append(
            {"id": rental_id,"asset_id": asset["id"],"start_date": start_date,"end_date": end_date}
        )
    return rentals


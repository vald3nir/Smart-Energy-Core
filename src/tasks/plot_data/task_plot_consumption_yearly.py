import matplotlib.pyplot as plt

from src.database import MongoDB
from src.tasks import get_time_series_collection_name


def plot_consumption_yearly(_user_name, _year):
    db = MongoDB(collection=get_time_series_collection_name(_user_name))

    date = []
    consumption = []
    consumption_total = 0

    for data in db.aggregate([
        {
            "$match": {
                "date": {
                    '$regex': f"{_year}-.*"
                }
            }
        },
        {
            "$group": {
                "_id": {
                    "$substr": ["$date", 0, 7]
                },
                "date": {
                    "$first": "$date"
                },
                "consumption_kwh": {
                    "$sum": "$consumption_kwh"
                },
            }

        },
        {
            "$sort": {
                "date": 1
            }
        }
    ]):
        date.append(data["_id"])
        consumption.append(data["consumption_kwh"])
        consumption_total += data["consumption_kwh"]

    plt.title(f"Year {_year}: {consumption_total} KW/h")
    plt.xticks(rotation='vertical')
    plt.ylabel('KW/h')
    plt.bar(date, consumption)
    plt.show()

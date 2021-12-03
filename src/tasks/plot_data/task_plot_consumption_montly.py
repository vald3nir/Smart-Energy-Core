import matplotlib.pyplot as plt

from src.database import MongoDB
from src.tasks import get_time_series_collection_name


def plot_consumption_monthly(_user_name, _date):
    db = MongoDB(collection=get_time_series_collection_name(_user_name))

    query = [
        {
            "$match": {
                "date": {
                    '$regex': f"{_date}-.*"
                }
            }
        },
        {
            "$group": {
                "_id": {
                    "$substr": ["$date", 0, 10]
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
    ]

    date = []
    consumption = []
    consumption_total = 0

    for data in db.aggregate(query):
        date.append(data["_id"][8:])
        consumption.append(data["consumption_kwh"])
        consumption_total += data["consumption_kwh"]

    plt.title(f"Month {_date}: {consumption_total} KW/h")
    plt.xticks(rotation='vertical')
    plt.ylabel('KW/h')
    plt.bar(date, consumption)
    plt.show()

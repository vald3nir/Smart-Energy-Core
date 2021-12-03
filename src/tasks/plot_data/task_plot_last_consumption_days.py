import matplotlib.pyplot as plt

from src.database import MongoDB
from src.tasks import get_time_series_collection_name


def plot_last_consumption_days(_user_name, num_days=30):
    db = MongoDB(collection=get_time_series_collection_name(_user_name))

    query = [
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
                "date": -1
            }
        },
        {
            "$limit": num_days
        }
    ]

    date = []
    consumption = []
    consumption_total = 0

    for data in db.aggregate(query):
        print(data["_id"], data["consumption_kwh"])
        date.append(data["_id"])
        consumption.append(data["consumption_kwh"])
        consumption_total += data["consumption_kwh"]

    date.reverse()
    consumption.reverse()

    plt.title(f"Consumption of last {num_days} days: {consumption_total} KW/h")
    plt.xticks(rotation='vertical')
    plt.ylabel('KW/h')
    plt.bar(date, consumption)
    plt.show()

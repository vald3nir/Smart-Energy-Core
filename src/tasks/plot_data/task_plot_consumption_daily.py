import matplotlib.pyplot as plt

from src.database import MongoDB
from src.tasks import get_time_series_collection_name


def plot_consumption_daily(_user_name, _date):
    db = MongoDB(collection=get_time_series_collection_name(_user_name))

    dates = []
    consumptions = []
    consumption_total = 0

    for data in db.find_all({"date": {'$regex': f'{_date}.*'}}):
        dates.append(data["date"][11:-9])
        consumptions.append(data["consumption_kwh"] * 1000)
        consumption_total += data["consumption_kwh"]

    plt.title(f"Total {consumption_total} KW/h")
    plt.xticks(rotation='vertical')
    plt.ylabel('W/h')
    plt.plot(dates, consumptions)
    plt.show()

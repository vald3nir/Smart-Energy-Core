import matplotlib.pyplot as plt

from src.database.MongoDB import MongoDB


def plot_consumption_yearly(device, _year):
    db = MongoDB(collection="consumption")

    date = []
    consumption = []
    consumption_total = 0

    query = [
        {
            "$match": {
                "device": device,
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
    ]

    for data in db.aggregate(query):
        date.append(data["_id"])
        consumption.append(data["consumption_kwh"])
        consumption_total += data["consumption_kwh"]

    plt.title(f"Year {_year}: {consumption_total} KW/h")
    plt.xticks(rotation='vertical')
    plt.ylabel('KW/h')
    plt.bar(date, consumption)
    plt.show()


def plot_consumption_monthly(device, _date):
    db = MongoDB(collection="consumption")

    query = [
        {
            "$match": {
                "device": device,
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


def plot_consumption_daily(device, _date):
    db = MongoDB(collection="consumption")

    dates = []
    consumptions = []
    consumption_total = 0

    for data in db.find_all({"device": device, "date": {'$regex': f'{_date}.*'}}):
        dates.append(data["date"][11:-9])
        consumptions.append(data["consumption_kwh"] * 1000)
        consumption_total += data["consumption_kwh"]

    plt.title(f"Total {consumption_total} KW/h")
    plt.xticks(rotation='vertical')
    plt.ylabel('W/h')
    plt.bar(dates, consumptions)
    plt.show()


def plot_last_consumption_days(device, num_days=30):
    db = MongoDB(collection="consumption")

    query = [
        {
            "$match": {"device": device},
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


def plot_last_consumption_months(device, num_months=30):
    db = MongoDB(collection="consumption")

    query = [
        {
            "$match": {"device": device},
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
                "date": -1
            }
        },
        {
            "$limit": num_months
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

    plt.title(f"Consumption of last {num_months} months: {consumption_total} KW/h")
    plt.xticks(rotation='vertical')
    plt.ylabel('KW/h')
    plt.bar(date, consumption)
    plt.show()
from src.database.Firebase import FirebaseClient
from src.database.MongoDB import MongoDB

firebase = FirebaseClient()


def _fill_annual_consumption(data_array_json):
    month_labels = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]

    annual_consumption = []
    for x in month_labels:
        annual_consumption.append({"month": x, "consumption_kwh": 0.0})

    for x in data_array_json:
        index = int(x["month"]) - 1
        month = month_labels[index]
        for y in annual_consumption:
            if y["month"] == month:
                y["consumption_kwh"] = x["consumption_kwh"]
                break

    return annual_consumption


def _export_annual_consumption(device):
    pipeline = [
        {
            "$match": {
                "device": device
            }
        },
        {
            "$group": {
                "_id": {"$substr": ["$date", 0, 7]},
                "date": {"$first": "$date"},
                "consumption_kwh": {"$sum": "$consumption_kwh"},
            }
        },
        {
            "$sort": {
                "date": 1
            }
        },
        {
            "$project":
                {
                    "year": {"$substr": ["$date", 0, 4]},
                    "month": {"$substr": ["$date", 5, 2]},
                    "consumption_kwh": "$consumption_kwh",
                }
        },
        {
            "$group": {
                "_id": "$year",
                "description":
                    {"$push": {"month": "$month", "consumption_kwh": "$consumption_kwh"}}
            }
        },
    ]
    for data in MongoDB("consumption").aggregate(pipeline):
        annual_consumption = _fill_annual_consumption(data["description"])
        year = data["_id"]

        firebase.insert(
            collection=f"consumption/{device}/annual_consumption",
            document=f"{year}",
            data={"year": year, "consumption": annual_consumption}
        )


def _export_monthly_consumption(device):
    pipeline = [
        {
            "$match": {
                "device": device
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
        },
        {
            "$project":
                {
                    "year": {"$substr": ["$date", 0, 4]},
                    "month": {"$substr": ["$date", 5, 2]},
                    "day": {"$substr": ["$date", 8, 2]},
                    "consumption_kwh": "$consumption_kwh",
                }
        },
        {
            "$group": {
                "_id": "$month",
                "year": {"$first": "$year"},
                "month": {"$first": "$month"},
                "consumption_kwh": {"$sum": "$consumption_kwh"},
                "days": {"$push": {"day": "$day", "consumption_kwh": "$consumption_kwh"}}
            }
        },
        {
            "$sort": {
                "year": 1,
                "month": 1,
            }
        },
    ]
    for data in MongoDB("consumption").aggregate(pipeline):
        year = data["year"]
        month = data["month"]
        firebase.insert(
            collection=f"consumption/{device}/monthly_consumption",
            document=f"{year}-{month}",
            data={"consumption_kwh": data["consumption_kwh"], "days": data["days"]}
        )


def export_data_to_firebase():
    print("Exporting to firebase")
    for device in MongoDB("consumption").distinct("device"):
        _export_annual_consumption(device)
        _export_monthly_consumption(device)

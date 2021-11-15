import matplotlib.pyplot as plt

from src.database import MongoDB

_user_name = "Valdenir"
year = 2021

if __name__ == '__main__':

    db = MongoDB(collection=f"{_user_name}_Consumption")

    date = []
    consumption = []
    consumption_total = 0

    for data in db.aggregate([
        {
            "$match": {
                "date": {'$regex': f"{year}-.*"}
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
                "consumption": {
                    "$sum": "$consumption"
                },
            }
        },
        {
            "$sort": {
                "date": 1
            }
        }
    ]):
        date.append(data["date"])
        consumption.append(data["consumption"])
        consumption_total += data["consumption"]

    plt.title(f"Total {consumption_total} KW/h [Year: {year}]")
    plt.xticks(rotation='vertical')
    plt.ylabel('KW/h')
    plt.bar(date, consumption)
    plt.show()

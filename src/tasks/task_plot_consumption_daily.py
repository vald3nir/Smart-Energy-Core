import matplotlib.pyplot as plt

from src.database import MongoDB

_user_name = "Valdenir"

if __name__ == '__main__':

    db = MongoDB(collection=f"{_user_name}_Consumption")

    date = []
    consumption = []
    consumption_total = 0

    for data in db.find_all({"date": {'$regex': '.*-11-.*'}}):  # find for all day in month 11
        date.append(data["date"])
        consumption.append(data["consumption"])
        consumption_total += data["consumption"]

    plt.title(f"Total {consumption_total} KW/h")
    plt.xticks(rotation='vertical')
    plt.ylabel('KW/h')
    plt.bar(date, consumption)
    plt.show()

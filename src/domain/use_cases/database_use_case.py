from src.data.repository.database.daos.time_series_dao import TimeSeriesDAO
from src.data.repository.database.daos.users_dao import UsersDAO
from src.data.repository.database import FirebaseClient

userDB = UsersDAO()
timeseriesDB = TimeSeriesDAO()


def backup_db():
    userDB.backup()
    timeseriesDB.backup()


def restore_db():
    userDB.restore()
    timeseriesDB.restore()


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


def export_time_series_to_firebase():
    firebase = FirebaseClient()
    print("Exporting to firebase")

    for device in timeseriesDB.distinct("device"):

        for data in timeseriesDB.get_annual_consumption(device):
            annual_consumption = _fill_annual_consumption(data["description"])
            year = data["_id"]

            firebase.insert(
                collection=f"consumption/{device}/annual_consumption",
                document=f"{year}",
                data={"year": year, "consumption": annual_consumption}
            )

        print(f"device: {device} -> export annual consumption")

        for data in timeseriesDB.get_monthly_consumption(device):
            year = data["year"]
            month = data["month"]
            firebase.insert(
                collection=f"consumption/{device}/monthly_consumption",
                document=f"{year}-{month}",
                data={"consumption_kwh": data["consumption_kwh"], "days": data["days"]}
            )

        print(f"device: {device} -> export monthly consumption")

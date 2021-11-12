import src.utils.utils_csv as utils_csv
from src.tasks import USERS_FOLDER
import matplotlib.pyplot as plt
import math

USER = "Valdenir"
YEAR = "2021"
MONTH = "11"
DAY = "11"

DATASET = f"{USERS_FOLDER}{USER}/time_series/{YEAR}/{MONTH}/{YEAR}-{MONTH}-{DAY}.csv"

DATABASE_NAME = 'smart_energy'
WATTS_SECONDS_TO_KILOWATT_HOURS = 2.778 * math.pow(10, -7)

if __name__ == '__main__':
    consumption = utils_csv.list_column_values(DATASET, "power")
    plt.plot(consumption)
    plt.show()

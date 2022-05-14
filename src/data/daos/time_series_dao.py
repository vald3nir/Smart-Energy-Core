from src.constants import TIME_SERIES_CSV
from src.data.database.MongoDB import MongoDB
from src.domain.utils import utils_csv


class TimeSeriesDAO(MongoDB):

    def __init__(self) -> None:
        super().__init__("timeseries")

    def backup(self):
        consumption = []

        for data_json in self.find_all(query={}, sort_field="date"):
            data_json.pop("_id")
            consumption.append(data_json)

        utils_csv.json_to_file_csv(TIME_SERIES_CSV, consumption)

    def restore(self):
        self.clear()
        self.insert_many(utils_csv.file_csv_to_json(TIME_SERIES_CSV))

    def get_annual_consumption(self, device):
        return self.aggregate(
            pipeline=[
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
        )

    def get_monthly_consumption(self, device):
        return self.aggregate(
            pipeline=[
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
        )

from src.tasks.plot_data.task_plot_consumption_daily import plot_consumption_daily
from src.tasks.plot_data.task_plot_consumption_montly import plot_consumption_monthly
from src.tasks.plot_data.task_plot_consumption_yearly import plot_consumption_yearly

_user_name = "Valdenir"


def run_plot_consumption_daily():
    plot_consumption_daily(_user_name=_user_name, _date="2021-11-18")


def run_plot_consumption_monthly():
    plot_consumption_monthly(_user_name=_user_name, _date="2021-10")


def run_plot_consumption_yearly():
    plot_consumption_yearly(_user_name=_user_name, _year="2021")


if __name__ == '__main__':
    run_plot_consumption_daily()
    # run_plot_consumption_monthly()
    # run_plot_consumption_yearly()

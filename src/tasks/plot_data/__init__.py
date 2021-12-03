from src.tasks.plot_data.task_plot_consumption_daily import plot_consumption_daily
from src.tasks.plot_data.task_plot_consumption_montly import plot_consumption_monthly
from src.tasks.plot_data.task_plot_consumption_yearly import plot_consumption_yearly
from src.tasks.plot_data.task_plot_last_consumption_days import plot_last_consumption_days
from src.tasks.plot_data.task_plot_last_consumption_months import plot_last_consumption_months

if __name__ == '__main__':
    _user_name = "Valdenir"

    plot_consumption_daily(_user_name=_user_name, _date="2021-11-18")
    # plot_consumption_monthly(_user_name=_user_name, _date="2021-10")
    # plot_consumption_yearly(_user_name=_user_name, _year="2021")
    # plot_last_consumption_days(_user_name=_user_name, num_days=5)
    # plot_last_consumption_months(_user_name, num_months=24)

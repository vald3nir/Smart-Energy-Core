from src.tasks.plot_data.task_plot_consumption_daily import plot_consumption_daily
from src.tasks.plot_data.task_plot_consumption_montly import plot_consumption_monthly
from src.tasks.plot_data.task_plot_consumption_yearly import plot_consumption_yearly

_user_name = "Valdenir"

plot_consumption_daily(_user_name=_user_name, _date="2021-11-18")

plot_consumption_monthly(_user_name=_user_name, _date="2021-10")

plot_consumption_yearly(_user_name=_user_name, _year="2021")


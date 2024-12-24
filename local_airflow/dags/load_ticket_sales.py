from airflow.decorators import dag, task
from pendulum import datetime
from airflow.datasets import Dataset
import time


@dag(
    dag_id="load_ticket_sales",
    max_active_runs=1,
    start_date=datetime(2023, 1, 1),
    is_paused_upon_creation=False,
    catchup=False,
    schedule_interval="*/10 * * * *",
)
def dag_test():
    @task(outlets=[Dataset("load_ticket_sales")])
    def end_task():
        time.sleep(150)

    end_task()


dag_test()

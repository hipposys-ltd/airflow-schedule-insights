from airflow.decorators import dag, task
from pendulum import datetime
import time


@dag(
    dag_id="load_box_office_reports",
    max_active_runs=1,
    start_date=datetime(2023, 1, 1),
    is_paused_upon_creation=True,
    catchup=False,
    schedule_interval=None,
)
def dag_test():
    @task
    def try_task():
        time.sleep(20)

    try_task()


dag_test()

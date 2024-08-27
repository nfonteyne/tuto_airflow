from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'nfonteyne',
    'retries': 5,
    'retry_delay':timedelta(minutes=2)
}
with DAG(
    dag_id='our_first_dag_v5',
    default_args=default_args,
    description='This is our first dag that we write',
    start_date=datetime(2024, 8, 25, 2),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo hello word, this is the first task!"
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command="echo hey, i m the task2 and i will be running after the task1"
    )

    task3 = BashOperator(
        task_id='third_task',
        bash_command='echo hey, i m the task3 and i will be running after the task1 at the same time as task2'
    )

    # task dependency method 1
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    # task dependency method 2
    # task1 >> task2
    # task1 >> task3

    # task dependency method 3
    task1 >> [task2, task3]



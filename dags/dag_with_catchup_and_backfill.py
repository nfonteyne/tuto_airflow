from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'nfonteyne',
    'retries': 5,
    'retry_delay':timedelta(minutes=5)
}
with DAG(
    dag_id='dag_with_catchup_and_backfill_V2',
    default_args=default_args,
    start_date=datetime(2024, 8, 20),
    schedule_interval='@daily',
    catchup=False
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo This is a simple bash command"
    )
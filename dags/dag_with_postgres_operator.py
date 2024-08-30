from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator


default_args = {
    'owner': 'nfonteyne',
    'retries': 5,
    'retry_delay':timedelta(minutes=2)
}
with DAG(
    dag_id='dag_with_postgres_operator_v01',
    default_args=default_args,
    description='This is our first dag that we write',
    start_date=datetime(2024, 8, 25, 2),
    schedule_interval='0 0 * * *'
) as dag:
    task1 = PostgresOperator(
        task_id='create_postgres_table',
        postgres_conn_id="postgres",
        sql="""
            create table if not exists dag_runs (
                dt date,
                dag_id character varying,
                primary key (dt, dag_id)
            )
        """
    )
    task1
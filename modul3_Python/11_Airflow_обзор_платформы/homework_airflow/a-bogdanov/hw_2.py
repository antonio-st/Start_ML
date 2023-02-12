"""
hw_2.py DAG
"""
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

with DAG(
        'hw_2_a-bogdanov',  # уникальное имя DAG
        default_args={
            'depends_on_past': False,
            'email': ['airflow@example.com'],
            'email_on_failure': False,
            'email_on_retry': False,
            'retries': 1,
            'retry_delay': timedelta(minutes=5),  # timedelta из пакета datetime
        },

        description='Lesson 11, Task 2',
        schedule_interval=timedelta(days=1),
        start_date=datetime(2022, 1, 1),
        catchup=False,

        tags=['Lesson_11_Task_2'],
) as dag:

    t1 = BashOperator(
        task_id='print_dir',
        bash_command='pwd', # передаем путь pwd в bash
    )


    def print_context(ds, **kwargs):
        print(kwargs)
        print(ds)
        return 'Whatever you return gets printed in the logs'

    t2 = PythonOperator(
        task_id='print_ds',
        python_callable=print_context, # передаем функцию print_context
    )


    t1 >> t2

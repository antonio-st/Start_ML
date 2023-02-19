"""
hw_7.py DAG
"""
from datetime import datetime, timedelta
from textwrap import dedent

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

with DAG(
        'hw_7_a-bogdanov',  # уникальное имя DAG
        default_args={
            'depends_on_past': False,
            'email': ['airflow@example.com'],
            'email_on_failure': False,
            'email_on_retry': False,
            'retries': 1,
            'retry_delay': timedelta(minutes=5),  # timedelta из пакета datetime
        },

        description='Lesson 11, Task 7',
        schedule_interval=timedelta(days=1),
        start_date=datetime(2022, 1, 1),
        catchup=False,

        tags=['Lesson_11_Task_7'],
) as dag:
    def print_context(ts, run_id, task_number):
        print(ts, run_id)
        return f"task number is: {task_number}"


    for i in range(20):
        t1 = PythonOperator(
            task_id='print_task_num_' + str(i),
            python_callable=print_context,  # передаем функцию print_context
            op_kwargs={'task_number': i}  # передаем значение i в функцию print_context в виде словаря
        )

    t1
"""
hw_6.py DAG
"""
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

with DAG(
        'hw_6_a-bogdanov',  # уникальное имя DAG
        default_args={
            'depends_on_past': False,
            'email': ['airflow@example.com'],
            'email_on_failure': False,
            'email_on_retry': False,
            'retries': 1,
            'retry_delay': timedelta(minutes=5),  # timedelta из пакета datetime
        },

        description='Lesson 11, Task 6',
        schedule_interval=timedelta(days=1),
        start_date=datetime(2022, 1, 1),
        catchup=False,

        tags=['Lesson_11_Task_6'],
) as dag:
    for i in range(10):
        t1 = BashOperator(
            task_id='print_in_bash_env_' + str(i),
            env = {'NUMBER': str(i)}, # создаем переменную окружения, передаем значение str(i) из цикла
            bash_command=f"echo $NUMBER", # передаем значение $NUMBER через $
        )


    t1

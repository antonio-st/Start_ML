"""
hw_12.py DAG
"""
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator



with DAG(
        'hw_12_a-bogdanov',  # уникальное имя DAG
        default_args={
            'depends_on_past': False,
            'email': ['airflow@example.com'],
            'email_on_failure': False,
            'email_on_retry': False,
            'retries': 1,
            'retry_delay': timedelta(minutes=5),  # timedelta из пакета datetime
        },

        description='Lesson 11, Task 12',
        schedule_interval=timedelta(days=1),
        start_date=datetime(2022, 1, 1),
        catchup=False,

        tags=['Lesson_11_Task_12'],
) as dag:
    def print_variables(var):
        from airflow.models import Variable
        is_startml = Variable.get("is_startml")
        print(is_startml)
        return 'is_startml variable print'

    t1 = PythonOperator(
        task_id='print_variable',
        python_callable=print_variables,  # передаем функцию print_variables
     )

    t1
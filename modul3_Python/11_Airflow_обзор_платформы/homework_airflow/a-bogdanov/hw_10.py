"""
hw_10.py DAG
"""
from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python import PythonOperator


# x_com отправляем данные неявно
def x_com_push(ti):
    ti.xcom_push(
        key='to_return_xcom_key',
    )
    return "Airflow tracks everything"


# xcom_pull принимаем данные
def x_com_pull(ti):
    data_read_push = ti.xcom_pull(
        key='return_value',
        task_ids='push_data_out',
    )
    print('Test xcom: ', data_read_push)


with DAG(
        'hw_10_a-bogdanov',  # уникальное имя DAG
        default_args={
            'depends_on_past': False,
            'email': ['airflow@example.com'],
            'email_on_failure': False,
            'email_on_retry': False,
            'retries': 1,
            'retry_delay': timedelta(minutes=5),  # timedelta из пакета datetime
        },

        description='Lesson 11, Task 10',
        schedule_interval=timedelta(days=1),
        start_date=datetime(2022, 1, 1),
        catchup=False,

        tags=['Lesson_11_Task_10'],
) as dag:
    # отправляем значения
    t1 = PythonOperator(
        task_id='push_data_out',
        python_callable=x_com_push
    )

    # принимаем значения
    t2 = PythonOperator(
        task_id='pull_data_in',
        python_callable=x_com_pull
    )

    t1 >> t2

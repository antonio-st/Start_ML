"""
hw_11.py DAG
"""
from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

from airflow.providers.postgres.operators.postgres import PostgresHook


def get_db():
    postgres = PostgresHook(postgres_conn_id="startml_feed")
    with postgres.get_conn() as conn:  # вернет тот же connection, что вернул бы psycopg2.connect(...)
        with conn.cursor() as cursor:
            cursor.execute(
                f"""
                    SELECT
                        user_id, 
                        COUNT(action)
                    FROM feed_action
                    WHERE action = 'like'
                    GROUP BY user_id
                    ORDER BY COUNT(action) DESC
                    LIMIT 1
                 """
            )
            return cursor.fetchall()


with DAG(
        'hw_11_a-bogdanov',  # уникальное имя DAG
        default_args={
            'depends_on_past': False,
            'email': ['airflow@example.com'],
            'email_on_failure': False,
            'email_on_retry': False,
            'retries': 1,
            'retry_delay': timedelta(minutes=5),  # timedelta из пакета datetime
        },

        description='Lesson 11, Task 11',
        schedule_interval=timedelta(days=1),
        start_date=datetime(2022, 1, 1),
        catchup=False,

        tags=['Lesson_11_Task_11'],
) as dag:
    # отправляем значения
    t1 = PythonOperator(
        task_id='get_db_req',
        python_callable=get_db
    )

    t1

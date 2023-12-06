# add this file to folder dags
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.exceptions import AirflowSkipException


args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 12, 5,),
}

dag = DAG(
    dag_id='task_1', default_args=args,
    schedule_interval="*/15 * * * *",)


def push_current_date_time(ds, **kwargs) -> datetime:
    """Вернуть текущее дату-время."""
    current_date_time = datetime.now()
    return current_date_time


first_task = PythonOperator(
    task_id='push_current_date_time',
    provide_context=True,
    python_callable=push_current_date_time,
    dag=dag)


def print_date_or_skip(ds, ti, **kwargs) -> str:
    """Получение даты или скип."""
    current_datetime = ti.xcom_pull(task_ids='push_current_date_time')
    if current_datetime.minute >= 30:
        print(current_datetime.date())
        return 'Finish'
    raise AirflowSkipException


second_task = PythonOperator(
    task_id='print_date_or_skip',
    provide_context=True,
    python_callable=print_date_or_skip,
    dag=dag)


first_task >> second_task

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator


def extract(ti):
    ti.xcom_push(key="message", value= "Hello from task1")

def load(ti):
    data = ti.xcom_pull(key= "message", task_ids= "test_extract")
    print(data)

with DAG(
    dag_id= "test_xcoms"
) as dag:
    task1= PythonOperator(
        task_id= "test_extract",
        python_callable= extract
    )
    task2= PythonOperator(
        task_id= "test_load",
        python_callable= extract
    )
    task1>>task2
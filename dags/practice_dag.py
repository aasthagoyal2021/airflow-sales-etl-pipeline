from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime
def task1():
    print("hi")
def task2():
    print("hello")
with DAG(
    dag_id= "practice_dag",
    start_date=datetime(2024, 1, 1),
    schedule= None,
    catchup= False
)as dag:
    t1= PythonOperator(
        task_id= "task1",
        python_callable= task1
    )
    t2= PythonOperator(
        task_id= "task2",
        python_callable= task2
    )
    t1>>t2

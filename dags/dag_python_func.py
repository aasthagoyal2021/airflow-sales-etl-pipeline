from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.standard.operators.python import PythonOperator

default_args= {
    'owner' : 'aastha',
    'retry': 5,
    'retry_delay':timedelta(minutes= 2),
    'start-time' : datetime(2026,1,1,2)
}


def greet(name, age):
    print(f"Hello, Airflow,I am {name} of age {age} years")

with DAG(
    dag_id = "python_func_dag",
    default_args= default_args
) as dag:
    task1= PythonOperator(
        task_id= "greet",
        python_callable= greet,
        op_kwargs= {
            'name': 'Aastha',
            'age': 24
        }
    )
    task1
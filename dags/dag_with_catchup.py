from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime, timedelta
from airflow import DAG
# from airflow.sdk import dag, task
default_args={
    "owner": "aastha",
    "retries": 5,
    "retry_delay" : timedelta(minutes= 4)
}

with DAG(
    default_args= default_args,
    dag_id= "dag_with_catchup_v2",
    start_date= datetime(2026,1,1),
    schedule= '@daily',
    catchup= False

) as dag:
    task1= BashOperator(
        task_id= "task1",
        bash_command= "echo simple bash command"
    )
    task1

# @dag(
#     default_args= default_args,
#     start_date= datetime(2026,5,2),
#     schedule= '@daily',
#     catchup= False
# )
# def hello_catchup():
#     @task()
#     def task1():
#         print("new bash command")
#     task1()
# dag_catchup_new= hello_catchup()


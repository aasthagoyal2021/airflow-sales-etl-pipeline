from airflow import DAG
from datetime import datetime, timedelta
# from airflow.operators.bash import BashOperator
from airflow.providers.standard.operators.bash import BashOperator

default_args= {
    'owner': 'aastha',
    'retries': 5,
    'retry_delay': timedelta(minutes= 2),
    # 'schedule_interval': "@daily"
}

with DAG(
    dag_id= "my_new_dag",
    description= "This is my new dag",
    default_args= default_args,
    start_date= datetime(2026,2,1,2)
    # schedule_interval= "@daily"

) as dag:
    task1 = BashOperator(
        task_id= "first_task",
        bash_command= "echo task 1"
    )
    task2= BashOperator(
        task_id= "second_task",
        bash_command= "echo task 2 after task 1"
    )
    task3= BashOperator(
        task_id= "third_task",
        bash_command= "echo task 3 after task 1 along with task 2"
    )

    task1.set_downstream(task2)
    task1.set_downstream(task3)

    # task1>>task2
    # task1>>task3

    # task1>>[task2,task3]

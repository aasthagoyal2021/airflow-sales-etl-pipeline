from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator


# def greet():
#     return "Jerry"

def get_name(ti):
    first_name= ti.xcom_push(key="first_name", value= "Aastha")
    last_name= ti.xcom_push(key= "last_name", value= "Goyal")

def greet2(ti):
    # name= ti.xcom_pull(task_ids= "greet") 
    first_name= ti.xcom_pull(task_ids= "get_name", key = "first_name")
    last_name= ti.xcom_pull(task_ids="get_name", key= "last_name")
    age= ti.xcom_pull(task_ids= "get_age", key= "age")
    # name= first_name + " " + last_name
    print(f"Hello,I m {first_name} {last_name} of age {age} years")

def get_age(ti):
    age= ti.xcom_push(key= "age", value=24)


with DAG(
    dag_id= "xcoms_in_dag"
) as dag:
    # task1= PythonOperator(
    #     task_id= "greet",
    #     python_callable= greet
    # )

    task2= PythonOperator(
        task_id= "greet2",
        python_callable= greet2
        # op_kwargs={'age':20}
    )
    task3= PythonOperator(
        task_id= "get_name",
        python_callable= get_name
    )
    task4= PythonOperator(
        task_id= "get_age",
        python_callable= get_age
    )
    [task3, task4] >> task2
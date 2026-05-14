from airflow import DAG
from airflow.providers.standard.sensors.filesystem import FileSensor
from airflow.providers.standard.operators.python import PythonOperator, BranchPythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.operators.empty import EmptyOperator
import pandas as pd

def extract():
    sales_df= pd.read_csv("/opt/airflow/output_files/sales_project/sales_input.csv")
    print(sales_df)

def validate():
    sales_df= pd.read_csv("/opt/airflow/output_files/sales_project/sales_input.csv")
    if sales_df.isnull().sum().sum()>0:
        return "invalid_task"
    return "transform_task"

def transform():
    df = pd.read_csv("/opt/airflow/output_files/sales_project/sales_input.csv")

    df["sales"] = df["price"] * df["quantity"]

    df.to_csv(
        "/opt/airflow/output_files/sales_project/transformed_sales.csv",
        index=False
    )

    print(df)

def load():
    df= pd.read_csv("/opt/airflow/output_files/sales_project/transformed_sales.csv")
    hook= PostgresHook(
        postgres_conn_id = "localhost_postgres_new"
    )
    conn= hook.get_conn()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales_data(
        order_id int primary key,
        price int,
        quantity int,
        sales float
        )
    '''
    )
    rows= df.values.tolist()
    cursor.executemany('''
        insert into sales_data(order_id, price,quantity,sales)
        values(%s, %s, %s, %s)
        on conflict (order_id) do nothing
    ''',
    rows
    )
    conn.commit()
    cursor.close()
    conn.close()




with DAG(
    dag_id= "sales_etl_pipeline"
) as dag:
    wait_for_file= FileSensor(
        task_id= "sense_file",
        fs_conn_id= "fs_sales",
        filepath = "sales_project/sales_input.csv",
        timeout = 60,
        poke_interval= 10
    )
    extract= PythonOperator(
        task_id= "extract_task",
        python_callable =  extract
    )
    validate= BranchPythonOperator(
        task_id= "validate_task",
        python_callable= validate
    )
    transform = PythonOperator(
        task_id="transform_task",
        python_callable=transform
    )
    invalid= EmptyOperator(
        task_id = "invalid_task"
    )
    load_to_postgres= PythonOperator(
        task_id= "load_to_postgres",
        python_callable= load
    )

    wait_for_file>>extract
    extract>> validate
    validate>>[transform, invalid]
    transform>>load_to_postgres

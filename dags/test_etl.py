from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
def extract():
    df= pd.DataFrame({
        "name": ["aastha", "ndjd","dmnfjfk"],
        "age": [16,23,26]
    })
    df.to_csv("/opt/airflow/output_files/raw_data.csv", index= False)
    print("raw file created")

def transform():
    df= pd.read_csv("/opt/airflow/output_files/raw_data.csv")
    df["bonus"]= df["age"] *0.1
    df.to_csv("/opt/airflow/output_files/transform_data.csv", index= False)
    print(df)

with DAG(
    dag_id= "test_etl"
) as dag:
    t1 = PythonOperator(
        task_id="extract_task",
        python_callable=extract
    )

    t2 = PythonOperator(
        task_id="transform_task",
        python_callable=transform
    )

    t1 >> t2









# from airflow import DAG
# from airflow.providers.postgres.operators.postgres import PostgresOperator
# from datetime import datetime
# with DAG(
#     dag_id= "test_postgres_dag".py
# ) as dag:
#     create_table= PostgresOperator(
#         task_id= "create_table",
#         postgres_conn_id= "localhost_postgres",
#         sql= """ CREATE table if not exists employee(
#             id int,
#             name VARCHAR(50) 
#         );
#         """
#     )
#     create_table
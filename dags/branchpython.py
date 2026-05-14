from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime
import os


def check_file():
    if os.path.exists("/opt/airflow/output_files/raw_data.csv"):
        return "file_exists"
    return "file_missing"


with DAG(
    dag_id="branching_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    check = BranchPythonOperator(
        task_id="check_file",
        python_callable=check_file
    )

    exists = EmptyOperator(task_id="file_exists")
    missing = EmptyOperator(task_id="file_missing")

    check >> [exists, missing]
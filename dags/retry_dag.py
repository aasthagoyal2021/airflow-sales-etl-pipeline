# # Sales Data Pipeline (Mini Production Style)
# Generate sales data
#         ↓
# Validate data
#         ↓
# Transform (add revenue)
#         ↓
# Branch (valid / invalid)
#         ↓
# Save result file
import pandas as pd
from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator, BranchPythonOperator
from airflow.providers.standard.operators.empty import EmptyOperator
def extract():
    df= pd.DataFrame({
        "order_id": [1,2,3],
        "price": [200,30,59],
        "quantity" :[16,10,11]
    })
    path= "/opt/airflow/output_files/sales_raw.csv"
    df.to_csv(path, index= False)
    return path

def validate():
    df = pd.read_csv("/opt/airflow/output_files/sales_raw.csv")
    if df.isnull().sum().sum()>0:
        return "invalid_task"
    return "transform_task"


def transform():
    df= pd.read_csv("/opt/airflow/output_files/sales_raw.csv")
    df["sales"]= df["price_unknown"] * df["quantity"]
    df.to_csv("/opt/airflow/output_files/sales_transform.csv", index= False)

default_args= {
    "retries" : 2,
    "retry_delay" : timedelta(minutes= 1)
}

with DAG(
    dag_id= "sales_etl_retry",
    schedule = "*/2 * * * *",
    catchup= False,
    start_date= datetime(2026,5,5),
    default_args= default_args
) as dag:
    extract= PythonOperator(
        task_id= "extract_task",
        python_callable= extract
    )
    validate= BranchPythonOperator(
        task_id= "validate_task",
        python_callable= validate
    )
    transform= PythonOperator(
        task_id= "transform_task",
        python_callable= transform
    )
    invalid= EmptyOperator(
        task_id= "invalid_task"
    )

    extract >> validate
    validate >>[invalid, transform]



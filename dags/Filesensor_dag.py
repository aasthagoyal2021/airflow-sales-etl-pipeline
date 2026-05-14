from airflow.providers.standard.sensors.filesystem import FileSensor
from airflow import DAG
from airflow.providers.standard.operators.empty import EmptyOperator
with DAG(
    dag_id= "file_sensor"
) as dag:
    check_file= FileSensor(
        task_id= "check_file",
        filepath = ("raw_data.csv"),
        # conn_id= "fs_default",
        timeout= 60,
        poke_interval = 10
    )
    next_task = EmptyOperator(
        task_id= "next_task"
    )
    check_file >> next_task
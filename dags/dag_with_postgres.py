from airflow import DAG
# from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator




with DAG (
    dag_id= "dag_with_postgres"
) as dag:
    task1= SQLExecuteQueryOperator(
        task_id= "create_table",
        conn_id= "localhost_postgres",
        sql= '''
            create table if not exists dag_runs(
                ds date,
                dag_id character varying,
                primary key(ds, dag_id)
            )
        '''
    )
    task2= SQLExecuteQueryOperator(
        task_id= "insert_table",
        conn_id= "localhost_postgres",
        sql= '''
            insert into dag_runs(ds, dag_id)
            values('{{ds}}', '{{dag.dag_id}}')
        '''
    )
    task3= SQLExecuteQueryOperator(
        task_id = "delete_table",
        conn_id= "localhost_postgres",
        sql= '''
            delete from dag_runs where ds= '{{ds}}' and dag_id= '{{dag.dag_id}}'
        '''
    )
    task1 >> task3 >> task2
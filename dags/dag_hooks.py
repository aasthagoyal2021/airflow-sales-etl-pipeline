# from airflow.providers.postgres.hooks.postgres import PostgresHook

# hook = PostgresHook(postgres_conn_id="localhost_postgres")
# conn = hook.get_conn()
# cursor = conn.cursor()

# cursor.execute("SELECT * FROM dag_runs")



from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime


def test_hook():
    hook = PostgresHook(postgres_conn_id="localhost_postgres")
    conn = hook.get_conn()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM dag_runs")    
    rows = cursor.fetchall()

    print(rows)


with DAG(
    dag_id="postgres_hook_dag",
    schedule=None,
    start_date=datetime(2026, 5, 5),
    catchup=False
) as dag:

    run_query = PythonOperator(
        task_id="run_query",
        python_callable=test_hook
    )
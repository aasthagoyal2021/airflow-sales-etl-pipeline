# from airflow import DAG
# from airflow.providers.standard.operators.python import PythonOperator
# from datetime import datetime
# from faker import Faker


# def test_faker():
#     fake = Faker()
#     print(fake.name())


# with DAG(
#     dag_id="faker_test",
#     start_date=datetime(2024, 1, 1),
#     schedule=None,
#     catchup=False
# ) as dag:

#     task1 = PythonOperator(
#         task_id="run_faker",
#         python_callable=test_faker
#     )








# from airflow import DAG
# from airflow.providers.standard.operators.python import PythonOperator
# from datetime import datetime
# from sklearn.linear_model import LinearRegression


# def test_sklearn():
#     model = LinearRegression()

#     X = [[1], [2], [3]]
#     y = [2, 4, 6]

#     model.fit(X, y)

#     print("Coefficient:", model.coef_)


# with DAG(
#     dag_id="sklearn_test",
#     start_date=datetime(2024, 1, 1),
#     schedule=None,
#     catchup=False
# ) as dag:

#     task1 = PythonOperator(
#         task_id="run_sklearn",
#         python_callable=test_sklearn
#     )








# from airflow import DAG
# # from airflow.operators.python import PythonOperator
# from airflow.providers.standard.operators.python import PythonOperator
# from datetime import datetime
# import pandas as pd


# def test_pandas():
#     df = pd.DataFrame({
#         "name": ["A", "B"],
#         "age": [10, 20]
#     })
#     print(df)


# with DAG(
#     dag_id="pandas_test",
#     start_date=datetime(2024, 1, 1),
#     schedule=None,
#     catchup=False
# ) as dag:

#     task1 = PythonOperator(
#         task_id="run_pandas",
#         python_callable=test_pandas
#     )
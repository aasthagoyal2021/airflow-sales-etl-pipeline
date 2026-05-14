from airflow.sdk import dag,task

@dag()
def hello_world_etl():
    @task(multiple_outputs= True)
    def get_name():
        return {
            "first_name":"Aastha",
            "last_name" : "Goyal"
        }
    @task()
    def get_age():
        return 25
    @task()
    def greet(first_name, last_name, age):
        print(f"hi i am {first_name} { last_name}, {age} years")

    dict_name= get_name()
    age= get_age()
    greet(first_name= dict_name["first_name"],
        last_name= dict_name["last_name"],
        age= age)
new_greet_dag= hello_world_etl()



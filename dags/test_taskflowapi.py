from airflow.sdk import dag, task
import pandas as pd
@dag(

)
def new_taskflow():
        @task
        def extract():
            df= pd.DataFrame({
                "order_id": [1,2,3],
                "price": [200,30,59],
                "quantity" :[16,10,11]
            })
            return df.to_dict()
        
        @task
        def transform(data):
            x= pd.DataFrame(data)
            x["bonus"]= x["price"] *0.1
            print(x.to_dict())

        data = extract()
        transform(data)

new_taskflow()



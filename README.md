
## **Prerequisites**

Before starting, make sure you have the following installed:

### **Step 0: Install Docker Desktop**

Download and install Docker Desktop:

* [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)

### **Step 1: Install Git (if not already installed)**

Download from:

* [https://git-scm.com/install/](https://git-scm.com/install/)

---


# Airflow Sales ETL Pipeline

Built an end-to-end ETL pipeline using Apache Airflow and PostgreSQL.

## Project Flow

sales_input.csv
↓
FileSensor waits for file
↓
Extract CSV data
↓
Validate null values
↓
Branch workflow
   - transform_task (valid data)
   - invalid_task (invalid data)
↓
Transform data (calculate sales = price * quantity)
↓
Load transformed data into PostgreSQL

## Tech Stack

- Apache Airflow
- PostgreSQL
- Python
- Pandas
- Docker

## Airflow Concepts Used

- FileSensor
- PythonOperator
- BranchPythonOperator
- EmptyOperator
- PostgresHook

## Features

- Waits for file arrival before pipeline execution
- Validates input data quality
- Conditional branching for invalid records
- Transforms sales data
- Loads data into PostgreSQL
- Handles duplicate inserts using ON CONFLICT

## Sample Input

order_id,price,quantity
1,100,2
2,200,3
3,150,1

## Output

Creates transformed file with sales column and loads records into PostgreSQL table:
sales_data


## Project Structure

airflow/
├── dags/
│   └── sales_project/
│       └── sales_pipeline.py
├── output_files/
│   └── sales_project/
│       ├── sales_input.csv
│       └── transformed_sales.csv

import pandas as pd
from sqlalchemy import create_engine

# Read the Excel data into a DataFrame
excel_data_df = pd.read_excel('/home/thirusubramaniyan/Desktop/zogx_project/bmi_calculator/dresses.xlsx', sheet_name='Sheet1')

# Database connection details
user = 'root'
password = 'zogx#123'
host = '68.183.245.71'
port = 3306
database = 'BMI_calculator'
table_name = 'dresses'

# Create the database connection
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")

# Bulk insert the data into the database table
excel_data_df.to_sql(name=table_name, con=engine, if_exists='append', index=False)

# Close the database connection
engine.dispose()



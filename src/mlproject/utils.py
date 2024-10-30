# import os
# import sys 
# from src.mlproject.exception import CustomException  # from exception.py import #*CustomException() function
# from src.mlproject.logger import logging # from logger.py import #*logging() function
# import pandas as pd
# from dotenv import load_dotenv # To load all environment
# import pymysql # To connect sql workbench with python


# load_dotenv()

# # it will get all This information from .env file
# host =os.getenv("host")
# user = os.getenv("user")
# password = os.getenv("password")
# db=os.getenv('db')


# def read_sql_data():  # This function will read data from sql files and this function get called in #* data ingestion
#     logging.info("Reading SQL database started...")
#     try:
#         mydb = pymysql.connect(
#             host = host,
#             user = user,
#             password = password,
#             db = db
            
#         )
#         logging.info("Connection Established",mydb)
#         df = pd.read_sql_query('Select * from students', mydb) # inbuilt pandas function to read sql data
#         print(df.head())
        
#         return df
        
#     except Exception as ex:
#         raise CustomException(ex)


import os
import sys
from src.mlproject.exception import CustomException  # from exception.py import CustomException function
from src.mlproject.logger import logging  # from logger.py import logging function
import pandas as pd
from dotenv import load_dotenv  # To load all environment variables
import pymysql  # To connect SQL workbench with Python

# Load environment variables from .env file
load_dotenv()

# Get SQL connection information from environment variables
host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")

def read_sql_data():  # This function reads data from SQL and is called in data ingestion
    logging.info("Reading SQL database started...")
    try:
        # Establish SQL connection
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info(f"Connection Established to database '{db}'")

        # Read SQL data into a pandas DataFrame
        df = pd.read_sql_query('SELECT * FROM students', mydb)
        print(df.head())

        # Close connection
        mydb.close()
        
        return df
        
    except Exception as ex:
        raise CustomException(ex, sys)

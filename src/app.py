import os
from sqlalchemy import create_engine
from sqlalchemy import text
import pandas as pd
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

def connect():
    global engine # This allows us to use a global variable called "engine"
    # A "connection string" is basically a string containing all database credentials together.
    connection_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}?autocommit=true"
    print("Starting the connection...", connection_string)
    engine = create_engine(connection_string)
    engine.connect()
    return engine

# 1) Connect to the database here using the SQLAlchemy's create_engine function
connection_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
print("Starting the connection...", connection_string)
engine = create_engine(connection_string)
engine.connect()

# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function
# with engine.connect() as con:
#     with open("sql/create.sql") as file:
#         query = text(file.read())
#         con.execute(query)

# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function
# with engine.connect() as con:
#     with open("sql/insert.sql") as file:
#         query = text(file.read())
#         con.execute(query)

# 4) Use pandas to print one of the tables as dataframes using read_sql function
result_dataFrame = pd.read_sql("SELECT * FROM publishers;", engine)
print(result_dataFrame)

""" Module contains a simple code snippet to interact with the managed instance using Azure login.

Requirements:
    1. Modules: pyodbc, azure-identity, python-dotenv.
    2. A .env file with SERVER_NAME, DATABASE_NAME, and USERNAME setup.

Note: This uses an interactive login step."""

import pyodbc
from azure.identity import InteractiveBrowserCredential
from dotenv import dotenv_values

config = {**dotenv_values(".env")}
server_name = config["SERVER_NAME"]
database_name = config["DATABASE_NAME"]
username = config["USERNAME"]
credential = InteractiveBrowserCredential()

conn_str = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server_name};"
    f"DATABASE={database_name};"
    "Authentication=ActiveDirectoryInteractive;"
    f"UID={username};"
)

query = "SELECT * FROM foo"

# Connect to the database
try:
    with pyodbc.connect(conn_str, credential=credential) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        print(row)
except pyodbc.Error as e:
    print(f"Error connecting to Azure SQL Database: {e}")

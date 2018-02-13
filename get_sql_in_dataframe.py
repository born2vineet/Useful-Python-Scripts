import pandas as pd
import pymssql

# The following function returns a pandas dataframe from a given query
def return_df_from_sql(server_name, database_name, sql):
    conn = pymssql.connect(server=server_name, database= database_name)
    df = pd.read_sql(sql, conn)
    return df
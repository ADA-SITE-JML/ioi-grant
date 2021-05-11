import matplotlib.pyplot as plt
from configs import *
import pandas as pd
import psycopg2
import sys

def connect(params_dic):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1) 
    print("Connection successful")
    return conn

def postgresql_to_dataframe(conn, select_query, column_names):
    """
    Tranform a SELECT query into a pandas dataframe
    """
    cursor = conn.cursor()
    try:
        cursor.execute(select_query)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        cursor.close()
        return 1

    # Naturally we get a list of tupples
    tupples = cursor.fetchall()
    cursor.close()

    # We just need to turn it into a pandas dataframe
    df = pd.DataFrame(tupples,  columns=column_names)
    df = df.dropna()
    return df


if __name__ == "__main__":
    
    query = sys.argv[1]
    column_names = None

    try:
        column_names = sys.argv[2].split(',') if sys.argv[2] else None
    except:
        pass

    # connection parameters, yours will be different
    params = {
        "host"      : host,
        "database"  : dbname,
        "user"      : user,
        "password"  : password
    } 

    conn = connect(params)

    df = postgresql_to_dataframe(conn, query, column_names)
    
    print(df.head())

    df.plot()
    plt.show()

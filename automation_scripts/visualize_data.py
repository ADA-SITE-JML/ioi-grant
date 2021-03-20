import matplotlib.pyplot as plt
import psycopg2
import pandas as pd
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

    # Connection parameters, yours will be different
    params = {
        "host"      : "192.168.33.115",
        "database"  : "cmsdb",
        "user"      : "cmsuser",
        "password"  : "cmspsw"
    }   

    conn = connect(params)

    df = postgresql_to_dataframe(conn, query, column_names)
    
    print(df.head())

    df.plot()
    plt.show()

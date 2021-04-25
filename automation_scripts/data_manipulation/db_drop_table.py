from config import *
import psycopg2
import json
import csv

if __name__ == "__main__":

    query = f"DROP TABLE IF EXISTS results;"

    try:
        conn = psycopg2.connect(host=host, user=user, password=password, dbname=dbname)

        cursor = conn.cursor()

        cursor.execute(query)

        print('Commit')
        conn.commit()

    except:
        pass
    
    finally:
        print('Closing cursor')
        cursor.close()

        print('Closing connection')
        conn.close()

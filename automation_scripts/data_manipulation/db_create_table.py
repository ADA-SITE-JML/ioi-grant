from config import *
import psycopg2
import json
import csv

if __name__ == "__main__":

    query = f"\
            CREATE TABLE results (\
                ranks INT NOT NULL,\
                user_id INT PRIMARY KEY,\
                full_name VARCHAR (255) NOT NULL,\
                country VARCHAR (255) NOT NULL,\
                shoes REAL NOT NULL,\
                split REAL NOT NULL,\
                rect REAL NOT NULL,\
                line REAL NOT NULL,\
                vision REAL NOT NULL,\
                walk REAL NOT NULL,\
                abs_score REAL NOT NULL,\
                rel_score REAL NOT NULL,\
                medals INT NOT NULL,\
                FOREIGN KEY (user_id) REFERENCES users (id)\
            );"

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

import psycopg2
import json
import csv

conn = psycopg2.connect(host='192.168.33.115', user='cmsuser', password='cmspsw', dbname='cmsdb')

cursor = conn.cursor()

create_query = f"\
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

cursor.execute(create_query)

print('Commit')
conn.commit()

print('Closing cursor')
cursor.close()

print('Closing connection')
conn.close()

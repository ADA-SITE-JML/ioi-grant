import psycopg2
import json
import csv

conn = psycopg2.connect(host='192.168.33.115', user='cmsuser', password='cmspsw', dbname='cmsdb')

cursor = conn.cursor()

query = f"DROP TABLE IF EXISTS results;"

cursor.execute(query)

print('Commit')
conn.commit()

print('Closing cursor')
cursor.close()

print('Closing connection')
conn.close()

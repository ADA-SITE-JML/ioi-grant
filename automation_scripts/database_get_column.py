import psycopg2
import json
import csv

conn = psycopg2.connect(host='192.168.33.115', user='cmsuser', password='cmspsw', dbname='cmsdb')

failers = []
medalists_ids_in_file_order = []
with open('medalists.csv', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        cursor = conn.cursor()

        for row in reader:
            splitted_ones = row[0].split()
    
            first_name, *last_name = splitted_ones
            last_name = " ".join(last_name)
            
            # we check wheter we have combined > 2 named people
            query = f"select * from users where first_name='{first_name}' and last_name='{last_name}';"
            cursor.execute(query)
            result = cursor.fetchall()
            if not result:
                # if not we try vice versa
                *first_name, last_name = splitted_ones     
                first_name = " ".join(first_name)

                # make request
                query = f"select * from users where first_name='{first_name}' and last_name='{last_name}';"
                cursor.execute(query)
                result = cursor.fetchall()
        

            if result:
                id, *_ = result[0]
                medalists_ids_in_file_order.append(id)
            else:
                medalists_ids_in_file_order.append(first_name + " " + last_name)
                failers.append(first_name + " " + last_name)

        print('Commiting changes')
        conn.commit()
        
        print('Closing cursor')
        cursor.close()

print('Closing connection')
conn.close()


print('Printing IDS:')
for id in medalists_ids_in_file_order:
    print(id)

print('Printing failures:')
for failer in failers:
    print(failer)

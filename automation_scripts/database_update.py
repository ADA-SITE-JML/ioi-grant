import psycopg2
import csv

conn = psycopg2.connect(host='localhost', user='cmsuser', password='cmspsw', dbname='cmsdb')

failers = []
with open('medalists.csv') as file:
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
            
            medal = row[1]
    
            query_update = f"update users set medals={medal} where first_name='{first_name}' and last_name='{last_name}';"
            cursor.execute(query_update)

            query = f"select * from users where first_name='{first_name}' and last_name='{last_name}';"
            cursor.execute(query)
            result = cursor.fetchall()

            if result:
                print(result)
            else:
                failers.append(first_name + " " + last_name)

        print('Commiting changes')
        conn.commit()
        
        print('Closing cursor')
        cursor.close()

print('Closing connection')
conn.close()

print('Printing failures:')
for failer in failers:
    print(failer)

from configs import *
import psycopg2
import json
import csv

if __name__ == "__main__":

    try:
        conn = psycopg2.connect(host=host, user=user, password=password, dbname=dbname)

        with open('medalist_results.csv', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter='\t')
            cursor = conn.cursor()
            
            # in this case first 2 rows are not data
            for row in list(reader)[2:]:

                rank, user_id, full_name, country, shoes, split, rect, line, vision, walk, abs_score, rel_score, medal = row[0].split(',')
        
                query = f"INSERT INTO results (ranks, user_id, full_name, country, shoes, split, rect, line, vision, walk, abs_score, rel_score, medals) \
                            VALUES ({rank}, {user_id}, '{full_name}', '{country}', {shoes}, {split}, {rect}, {line}, {vision}, {walk}, {abs_score}, {rel_score}, {medal});"

                cursor.execute(query)

    except:
        pass
    
    finally:

        print('Commiting')
        conn.commit()
        
        print('Closing cursor')
        cursor.close()

        print('Closing connection')
        conn.close()
from configs import *
import psycopg2
import json
import csv
import sys



if __name__ == "__main__":
    """
    The below operations are responsible to find the users in the database upon firstname and lastname. The id of the matched users are stored in a csv file.
    """

    file_name = sys.argv[1]

    try:
        conn = psycopg2.connect(host=host, user=user, password=password, dbname=dbname)

        failers = []
        medalists_ids_in_file_order = []
        with open(file_name, encoding='utf-8') as file:
            reader = csv.reader(file, delimiter='\t')
            cursor = conn.cursor()

            for row in list(reader)[2:]:
                splitted_ones = row[0].split(',')

                full_name = splitted_ones[2].split()
                first_name, last_name = [None] * 2
                result = None

                for i in range(1, len(full_name)):
                    first_name, last_name = " ".join(full_name[:i]), " ".join(full_name[i:])
                    query = f"select * from users where upper(first_name)='{first_name.upper()}' and upper(last_name)='{last_name.upper()}';"
                    cursor.execute(query)
                    result = cursor.fetchall()
                    if len(result) == 1: break

                if result:
                    id, *_ = result[0]
                    medalists_ids_in_file_order.append(id)
                else:
                    medalists_ids_in_file_order.append(f'{first_name} {last_name}')
                    failers.append(full_name)

            print('Commiting changes')
            conn.commit()
    except:
        pass

    finally:           
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
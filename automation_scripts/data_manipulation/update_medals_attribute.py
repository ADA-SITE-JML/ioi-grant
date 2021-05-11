from configs import *
import psycopg2
import csv



if __name__ == "__main__":
    """
    The below operations are responsible to find the users in the database upon firstname and lastname. Each matched instance is updated with a medals attribute.
    1 - GOLD
    2 - SILVER
    3 - BRONZE
    """

    file_name = sys.argv[1]

    try:
        conn = psycopg2.connect(host=host, user=user, password=password, dbname=dbname)

        failers = []
        with open(file_name) as file:
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
        
    except:
        pass

    finally:
        print('Closing cursor')
        cursor.close()

        print('Closing connection')
        conn.close()

        print('Printing failures:')
        for failer in failers:
            print(failer)

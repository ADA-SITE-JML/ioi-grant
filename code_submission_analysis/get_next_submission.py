import psycopg2

conn = psycopg2.connect(database="cmsdb", user="cmsuser",
                        password="cmspsw", host="192.168.33.115", port="5432")

cur = conn.cursor()

cur.execute("SELECT * from submissions")

rows = cur.fetchall()

import psycopg2

conn = psycopg2.connect(database="cmsdb", user="cmsuser",
                        password="cmspsw", host="192.168.33.115", port="5432")

cur = conn.cursor()

cur.execute("SELECT * from submissions")

rows = cur.fetchall()

# 1.get 1 after the latest fetched submission
# 2.check if it the user made submission has a prev submission on the same task
# 3.if yes then fetch that submission and return their add in filesystem
# 4.if no then return only that submission


# 1.1 Store last fetched submission in a file
# 1.2 add functionality to reset that value

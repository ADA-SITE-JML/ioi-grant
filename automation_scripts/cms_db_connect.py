import psycopg2


def create_connection():
    conn = psycopg2.connect(host='192.168.33.115', user='cmsuser', password='cmspsw', dbname='cmsdb')

    cur = conn.cursor()

    cur.execute("select * from users")

    print(cur.fetchone())


# if __name__ == "__main__":

#     create_connection()


# ssh_host_key = 'ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHoabOQ2YoMUvEAywrifT1nSfyoL/wIczNZa/EUsPFUki0KaUkBmu8a9Tbr3qIJXLPkgU/xwPuz+u7BTnJfw2GQ='

# with SSHTunnelForwarder(('192.168.33.115', 22), ssh_username="abagiyev", ssh_password="8nfDt79F", remote_bind_address=('localhost', 5432)) as server: 
#     server.start()

from sshtunnel import SSHTunnelForwarder

server = SSHTunnelForwarder(
    ('192.168.33.115', 22),
    ssh_username="abagiyev", 
    ssh_password="8nfDt79F", 
    remote_bind_address=("192.168.33.115", 5432)
) 
server.start()
create_connection()
# "SELECT date_trunc('hour', q.question_timestamp) + (((date_part('minute', q.question_timestamp)::integer / 30::integer) * 30::integer) || ' minutes')::interval AS time_grp, unnest(regexp_matches(q.subject, '#(\w{1,})', 'g')) as tags, count(*) FROM (SELECT id, subject, question_timestamp FROM questions  WHERE subject  LIKE '%#%' UNION SELECT id, REGEXP_REPLACE(subject, '.*', '#Clarifications') as subject, question_timestamp FROM questions  WHERE subject  NOT LIKE '%#%') as q WHERE q.question_timestamp >= (SELECT start FROM contests WHERE id = 2) AND q.question_timestamp <= (SELECT stop FROM contests WHERE id = 2) GROUP BY time_grp, tags ORDER BY time_grp;"
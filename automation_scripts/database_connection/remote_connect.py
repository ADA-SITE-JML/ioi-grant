from configs import *
import psycopg2

def create_connection():
    conn = psycopg2.connect(host=host, user=user, password=password, dbname=dbname)

    cur = conn.cursor()

    cur.execute("select * from users")

    print(cur.fetchone())


from sshtunnel import SSHTunnelForwarder
if __name__ == "__main__":

    server = SSHTunnelForwarder(
        (ssh_ip_address, ssh_port),
        ssh_username=ssh_username, 
        ssh_password=ssh_password, 
        remote_bind_address=remote_bind_address
    ) 
    server.start()
    create_connection()
    
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import psycopg2
import base64
import io


# method to connect to the CMS database
def connect(kwargs):
    """ Connect to the PostgreSQL database server """
    conn = None

    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')

        conn = psycopg2.connect(**kwargs)

        print("Connection successful")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return conn



def db_to_dataframe(credentials, query):
    """
    Tranform a SELECT query into a pandas dataframe
    """
    conn = connect(credentials)

    cursor = conn.cursor()

    try:
        cursor.execute(query)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)

        cursor.close()

        return

    # naturally we get a list of tupples
    tupples = cursor.fetchall()

    # get column names
    columns = [desc[0] for desc in cursor.description]

    # close cursor
    cursor.close()

    # we just need to turn it into a pandas dataframe
    df = pd.DataFrame(tupples,  columns=columns)

    return df


def fig_to_base64(fig):
    img = io.BytesIO()
    fig.savefig(img, format='png',
                bbox_inches='tight')
    img.seek(0)

    return base64.b64encode(img.getvalue())


def generate_dataframe_and_graph_as_base64(connection, query, code):
    global fig, ax, df

    df      = db_to_dataframe(connection, query)
    fig, ax = plt.subplots(figsize=(20, 10))

    exec(code, globals())

    encoded = fig_to_base64(fig)

    return df, 'data:image/png;base64, {}'.format(encoded.decode('utf-8'))

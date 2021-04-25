import matplotlib.pyplot as plt
from configs import *
import pandas as pd
import numpy as np
import psycopg2
import sys


GLOBAL_PARAMS = {}

def connect(params_dic):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1) 
    print("Connection successful")
    return conn

def postgresql_to_dataframe(conn, select_query):
    """
    Tranform a SELECT query into a pandas dataframe
    """
    cursor = conn.cursor()
    try:
        cursor.execute(select_query)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        cursor.close()
        return 1

    # Naturally we get a list of tupples
    tupples = cursor.fetchall()

    # get column names
    columns = [desc[0] for desc in cursor.description]

    # close cursor
    cursor.close()

    # We just need to turn it into a pandas dataframe
    df = pd.DataFrame(tupples,  columns=columns)

    del df['preferred_languages']

    # drop duplicated rows created by join
    df = df.T.drop_duplicates().T


    # save durations and tasks in a list to preserve the order    
    df = df.merge(df.groupby("country").agg(usernames=('username', list), abs_scores=('abs_score',list)).reset_index())

    # remove duplicates
    df = df.groupby(['country'], as_index=False).first()

    # add necessary attributes
    df['max_score']             = list(map(max, df['abs_scores']))
    df['min_score']             = list(map(min, df['abs_scores']))
    df['min_max_difference']    = df.max_score - df.min_score
    df['score_effectiveness']   = df.max_score + df.min_score

    # df = df.sort_values(by=['max_score', 'min_max_difference'], ascending=[False, True])
    df = df.sort_values(by=['score_effectiveness'], ascending=[False])

    return df

def get_cmap(n, name='hsv'):
    '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct 
    RGB color; the keyword argument name must be a standard mpl colormap name.'''
    return plt.cm.get_cmap(name, n)

def process_graph(df):
    """
    Parameters
    ----------
    results         : dict object which is contains users id and duration list
    colors          : dict object which contains task order list items as a key and assigned color hexadecimal(this is exactly the same order the way results has been done)
    tasks_colors    : dict object which contains unique task names and their mapped color
    """

    # PLOTTING
    fig, ax = plt.subplots(figsize=(9.2, 5))
    
    # Add an x-label to the axes.
    ax.set_xlabel('Countries', fontsize=14)

    # add a y-label to the axes.
    ax.set_ylabel('Scores', fontsize=14)

     # add a title to the axes.
    # ax.set_title(f"TITLE") 
    ax.invert_yaxis()
 
    # Set the axes ranges and axes labels
    
    ax.set_ylim(np.min(df.min_score) - 50, np.max(df.max_score) + 50)

    ax.set_xlim(0.5, len(df) + 0.5)

    ax.set_xticklabels(df.username.str[:3], rotation=45, fontsize=10)

    plots = ax.boxplot(df.abs_scores, patch_artist=True )

    # coloring the plots
    cmap = get_cmap(len(plots['boxes']))
    for index, box in enumerate(plots['boxes']):
        box.set_facecolor(cmap(index))

    return fig, ax

if __name__ == "__main__":
    # connection parameters, yours will be different
    params = {
        "host"      : host,
        "database"  : dbname,
        "user"      : user,
        "password"  : password
    }

    conn = connect(params)

    GLOBAL_PARAMS['contest_id'] = 2
    GLOBAL_PARAMS['medal'] = 1

    
    query = f"\
                SELECT * \
                FROM users \
                JOIN results \
                ON id=user_id \
                WHERE results.medals != 0; \
            "

    df = postgresql_to_dataframe(conn, query)
    
    print(df.head())

    # params = prepare_and_visualize(df)
    process_graph(df)

    # visualizing the final plot
    plt.show()
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import psycopg2
import sys

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

def postgresql_to_dataframe(conn, select_query, column_names):
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

    cursor.close()

    if column_names:
        columns = column_names
    else: 
        columns = [desc[0] for desc in cursor.description]

    # We just need to turn it into a pandas dataframe
    df = pd.DataFrame(tupples,  columns=columns)

    return df

def test(df, fig, ax):
    df.rename(columns={'time_grp': 'Time', 'name':'Task', 'count':'Count'}, inplace=True)

    df.set_index('Time')
    
    ax.set(ylim=(0, 140))

    for task in df['Task'].unique():
        day = df[df['Task'] == task]
        sns.lineplot(x='Time',y='Count',data=day, label='Submitted')
        ax = sns.lineplot(x='Time',y='Count',data=day, label='Scored')
        ax.lines[1].set_linestyle("--")
        leg = ax.legend()
        leg_lines = leg.get_lines()
        leg_lines[1].set_linestyle("--")
        ax.set_title('Day 1')
        ax.set(ylim=(0, 500))
        ax.set(xlabel=None,ylabel='Attempts')

if __name__ == "__main__":
    
    # query = sys.argv[1]
    query = "SELECT \
            date_trunc('hour', subs.timestamp) + (((date_part('minute', subs.timestamp)::integer / 30::integer) * 30::integer) || ' minutes')::interval AS time_grp, \
            (select name from tasks where id = subs.task_id), \
            count(*) FILTER (WHERE subs.score > 0), \
            MAX(score) \
            FROM \
            (SELECT s.id as submission_id, MAX(res.score) score, s.timestamp, s.task_id \
            FROM submissions s \
            INNER JOIN submission_results res \
            ON s.id = res.submission_id \
            WHERE EXTRACT(DAY FROM s.timestamp) = 6 \
            AND s.timestamp >= (SELECT start FROM contests WHERE id = 2) \
            AND s.timestamp <= (SELECT stop FROM contests WHERE id = 2) \
            AND s.official = TRUE \
            GROUP BY s.id) as subs \
            GROUP BY time_grp, task_id \
            ORDER BY time_grp;" 

    column_names = None

    try:
        column_names = sys.argv[2].split(',') if sys.argv[2] else None
    except:
        pass

    # connection parameters, yours will be different
    params = {
        'host'        : '192.168.33.115',
        'user'        : 'cmsuser',
        'password'    : 'cmspsw',
        'dbname'      : 'cmsdb',
    } 

    conn = connect(params)

    df = postgresql_to_dataframe(conn, query, column_names)

    print(df)

    fig, ax = plt.subplots(figsize=(8,5))

    test(df, fig, ax)

    # df.plot(ax = ax)

    # print(df.to_html())

    plt.show()

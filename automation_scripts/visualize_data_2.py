import matplotlib.pyplot as plt
import numpy as np
import psycopg2
import pandas as pd
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

    # drop duplicated rows created by join
    df = df.T.drop_duplicates().T

    # dropping NaN values, basically users withoout medals
    df = df.dropna()

    # compute to convert durations to minutes
    hours, remainder = divmod(df['time_spent_for_the_task'].dt.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    minutes = hours * 60 + minutes
    
    # compute to erase the day, month, year
    # df['start'] = df[5].dt.strftime('%H:%M:%S')

    # add new named colums
    df['task']      = df['task_name']
    df['duration']  = minutes

    # save durations and tasks in a list to preserve the order    
    df = df.merge(df.groupby("participation_id").agg(task_order=('task', list), durations=('duration',list)).reset_index())

    return df


def prepare_and_visualize(df):
    """
        blue   -> #0000ffff
        orange -> #ffa500ff 
        green  -> #006347ff
        white  -> #ffffffff
    """

    if GLOBAL_PARAMS['contest_id'] == 1:
        # contest 1
        task_names  = ['line', 'walk', 'vision']
        task_colors = ['#0000ffff', '#006347ff', '#ffa500ff']
    else:
        # contest 2
        task_names  = ['rect', 'split', 'shoes']
        task_colors = ['#ff0000ff', '##A309EFff', '##1D012Cff']

    # map duration to user ids
    user_durations_mapping  = {f"{row['full_name']}": row['durations'] for index, row in df.iterrows()}

    # map colors to tasks
    task_color_mapping      = {task: color for (task, color) in zip(task_names, task_colors)} 
    
    # creating appropriate color array
    color_list = [[task_color_mapping[task] for task in tasks] for tasks in df.task_order]

    return (user_durations_mapping, color_list, task_color_mapping)

def RGBA_convert(hex):
    hex = hex.lstrip('#')
    return [round(int(hex[i:i+2], 16) / 255, 8)  for i in (0, 2, 4, 6)]


def process_graph(results, colors, tasks_colors):
    """
    Parameters
    ----------
    results         : dict object which is contains users id and duration list
    colors          : dict object which contains task order list items as a key and assigned color hexadecimal(this is exactly the same order the way results has been done)
    tasks_colors    : dict object which contains unique task names and their mapped color
    """
    labels = list(results.keys())

    # finding maximum array lenght in the dictionary
    max_arr_length = max(map(len, results.values()))

    # since duration and tasks mapping are equal, the max will have the same size

    # add 0 for the short lists
    data   = np.array([np.pad(v, (0, max_arr_length - len(v)), 'constant', constant_values=(0)) for v in results.values()])

    # make each color list size equal to maximum length by feeling them with white color
    colors_list = np.array([np.pad(v, (0, max_arr_length - len(v)), 'constant', constant_values=('#ffffffff')) for v in colors])

    colors_list_trans = np.transpose(colors_list)
    
    # after having all array size equal, they need to be converted to list of 0-1 range representations
    colors_final = np.array([[RGBA_convert(color) for color in row] for row in colors_list_trans])

    # calculating cummulative sum
    data_cum = data.cumsum(axis=1)

    # PLOTTING
    fig, ax = plt.subplots(figsize=(9.2, 5))
    
    # Add an x-label to the axes.
    ax.set_xlabel('Durations (in minute)')

    # add a y-label to the axes.
    ax.set_ylabel('Medalists')

     # add a title to the axes.
    ax.set_title(f"Visualization of the day {GLOBAL_PARAMS['contest_id']} task switch by Gold Medalists on a timeline") 
 
    # make lowest user index to be at the top on y axis
    ax.invert_yaxis()
    
    # set maximum limit(calculate maximum of the data)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    for i in range(max_arr_length):
        widths = data[:, i]

        starts = data_cum[:, i] - widths
        
        ax.barh(labels, widths, left=starts, height=0.5, color=colors_final[i])
        
        xcenters = starts + widths / 2

        text_color = 'white' 

        for y, (x, c) in enumerate(zip(xcenters, widths)):
            if c:
                ax.text(x, y, str(int(c)), ha='center', va='center', color=text_color)
                
    ax.legend(tasks_colors, ncol=len(tasks_colors.keys()), bbox_to_anchor=(0.5, 0), loc='lower center', fancybox=True, shadow=True, fontsize='medium')
    
    return fig, ax

if __name__ == "__main__":
    # connection parameters, yours will be different
    params = {
        "host"      : "192.168.33.115",
        "database"  : "cmsdb",
        "user"      : "cmsuser",
        "password"  : "cmspsw"
    }   

    conn = connect(params)

    GLOBAL_PARAMS['contest_id'] = 2
    GLOBAL_PARAMS['medal'] = 1

    
    query = f"\
                SELECT * \
                FROM sub_stats \
                INNER JOIN results \
                ON sub_stats.user_id = results.user_id \
                WHERE sub_stats.medal={GLOBAL_PARAMS['medal']} and contest_id={GLOBAL_PARAMS['contest_id']}\
                ORDER BY ranks, sub_stats.user_id, last_submission_ts;\
            "

    df = postgresql_to_dataframe(conn, query)
    
    # eliminate duplicates
    df = df.groupby(['participation_id'], as_index=False).first()

    # make sure order is correct
    df = df.sort_values(by=['ranks', 'abs_score'])

    print(df.head())

    params = prepare_and_visualize(df)

    process_graph(*params)

    # visualizing the final plot
    plt.show()
import matplotlib.pyplot as plt
import numpy as np
import psycopg2
import pandas as pd
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

    # We just need to turn it into a pandas dataframe
    df = pd.DataFrame(tupples,  columns=column_names)

    # dropping NaN values, basically users withoout medals
    df = df.dropna()

    # compute to convert durations to minutes
    hours, remainder = divmod(df[2].dt.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    minutes = hours * 60 + minutes
    
    # compute to erase the day, month, year
    # df['start'] = df[5].dt.strftime('%H:%M:%S')

    # add new named colums
    df['user_id']   = df[0]
    df['tasks']     = df[1]
    df['duration']  = minutes

    # save durations and tasks in a list to preserve the order    
    df = df.merge(df.groupby("user_id").agg(task_order=('tasks', list), durations=('duration',list)).reset_index())

    return df


def prepare_and_visualize(df):
    """
        blue   -> #0000ffff
        orange -> #ffa500ff 
        green  -> #006347ff
        white  -> #ffffffff
    """

    task_names  = ['line', 'walk', 'vision']
    task_colors = ['#0000ffff', '#006347ff', '#ffa500ff']

    # map duration to user ids
    user_durations_mapping  = {f"User {row['user_id']}": row['durations'] for index, row in df.iterrows()}

    # map colors to tasks
    task_color_mapping      = {task: color for (task, color) in zip(task_names, task_colors)} 
    
    # creating appropriate color array
    color_list = [[task_color_mapping[task] for task in tasks] for tasks in df.task_order]

    process_graph(user_durations_mapping, color_list, task_color_mapping)

    # visualizing the final plot
    plt.show()


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
    ax.set_xlabel('Durations (in minutes)')

    # add a y-label to the axes.
    ax.set_ylabel('Users')

     # add a title to the axes.
    ax.set_title("Visualization of the task switch by Gold Medalists  on a timeline") 
 
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

    query = "\
                SELECT user_id, task_name, time_spent_for_the_task \
                FROM temp2 \
                WHERE medal=1 and contest_id=1 \
                ORDER BY user_id, last_submission_ts;\
            "

    df = postgresql_to_dataframe(conn, query, column_names=None)
    
    print(df.head(20))

    prepare_and_visualize(df)
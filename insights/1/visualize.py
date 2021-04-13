import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ioi_data = pd.read_csv('ioi-2019-submitted.csv')

for task in ioi_data['Task'].unique():
    day1 = ioi_data[ioi_data['Task']==task]
    plt.figure(figsize=(6,4))
    sns.lineplot(x='Time',y='Submitted',data=day1, label='Submitted')
    ax = sns.lineplot(x='Time',y='Scored',data=day1, label='Scored')
    ax.lines[1].set_linestyle("--")
    leg = ax.legend()
    leg_lines = leg.get_lines()
    leg_lines[1].set_linestyle("--")
    ax.set_title(task)
    ax.set(ylim=(0, 500))
    ax.set(xlabel=None,ylabel='Attempts')
    plt.show()

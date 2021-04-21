# Insight 2 (Contestant Requests)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ioi_data = pd.read_csv('ioi-requests.csv',index_col='Time')

for cd in ioi_data['Contest'].unique():
    day = ioi_data[ioi_data['Contest']==cd].groupby(by=['Time','Requests']).agg({"Count":"sum"}).sort_values(['Time'],ascending=True)
    plt.figure(figsize=(8,5))
    ax = sns.lineplot(data=day, x = "Time", y="Count", hue="Requests", style="Requests")
    ax.set(ylim=(0, 140))
    plt.show()

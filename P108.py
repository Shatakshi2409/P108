import pandas as pd
import csv
import plotly.figure_factory as ff

df=pd.read_csv('data1.csv')
ratinglist=df['attempt'].tolist()
fig=ff.create_distplot([ratinglist],['attempt'],show_hist=False)
fig.show()
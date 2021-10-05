import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
sort =  df.groupby("level")["attempt"].mean()
fig = go.Figure(go.Bar(
    x = sort,
    y=['level 1', 'level 2', 'level 3', 'level 4'],
    orientation ='h'
))
#fig.show()

student_data=df.loc[df['student_id']=="TRL_zet"]
student_mean=student_data.groupby("level")["attempt"].mean()
fig2= go.Figure(go.Bar(
    x=student_mean,
    y=['level 1', 'level 2', 'level 3', 'level 4'],
    orientation= 'h'
))
fig2.show()
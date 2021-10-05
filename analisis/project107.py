import pandas as pd
import csv
import plotly.graph_objects as go
import plotly.express as px

df = pd.read_csv("data.csv")
std_mean= df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
fig=px.scatter(
    std_mean, 
    x="student_id", 
    y="level", 
    size="attempt", 
    color="attempt")
fig.show()
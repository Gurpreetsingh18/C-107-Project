import pandas as pd 

import plotly.graph_objects as pg

df = pd.read_csv("data.csv")


print(df.groupby("level")["attempt"].mean())

fig= pg.Figure(
    pg.Bar(
        x=df.groupby("level")["attempt"].mean(),y=["level1","level2","level3","level4"],
        orientation='h'
    )
)
fig.show()

student_id = input("Please enter the student id : ")

print(student_id)
sd= df.loc[df["student_id"]==student_id]
fig= pg.Figure(
    pg.Bar(
        x=sd.groupby("level")["attempt"].mean(),y=["level1","level2","level3","level4"],
        orientation='h'
    )
)
fig.show()
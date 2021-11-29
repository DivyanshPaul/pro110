import pandas as pd
import csv
import plotly.figure_factory as pff
import statistics as st 
df=pd.read_csv("data.csv")
result=df["temp"].tolist()
fig=pff.create_distplot([result],["degrees"],show_hist=False)
population_mean=st.mean(result)

print(population_mean)
std=st.stdev(result)
print(std)
#fig.show()
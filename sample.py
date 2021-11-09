import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import csv

df=pd.read_csv("StudentsPerformance.csv")
reading_score=df["reading score"].tolist()
mean=statistics.mean(reading_score)
median=statistics.median(reading_score)
mode=statistics.mode(reading_score)
standardDeviation=statistics.stdev(reading_score)
print("mean=",mean)
print("median=",median)
print("mode=",mode)
print("standard deviation=",standardDeviation)
first_std_deviation_start, first_std_deviation_end = mean-standardDeviation, mean+standardDeviation
second_std_deviation_start, second_std_deviation_end = mean-(2*standardDeviation), mean+(2*standardDeviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*standardDeviation), mean+(3*standardDeviation)

fig = ff.create_distplot([reading_score], ["Result"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.show()

list_of_data_within_1_std_deviation = [result for result in reading_score if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in reading_score if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in reading_score if result > third_std_deviation_start and result < third_std_deviation_end]

print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(reading_score)))
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_within_2_std_deviation)*100.0/len(reading_score)))
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_3_std_deviation)*100.0/len(reading_score)))
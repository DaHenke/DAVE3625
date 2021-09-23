#3. Time series
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
url = "https://raw.githubusercontent.com/umaimehm/Intro_to_AI_2021/main/Lab3/data/flight.csv"
df = pd.read_csv(url, sep=',')

df['datetime_val'] = pd.to_datetime(df['datetime_val'], errors='coerce')
df['dep_time'] = pd.to_datetime(df['dep_time'], errors='coerce')
df['arr_time'] = pd.to_datetime(df['arr_time'], errors='coerce')
df['sched_arr_time'] = pd.to_datetime(df['sched_arr_time'], errors='coerce')

df['air_time'] = df.arr_time-df.dep_time

print(df[['dep_time','arr_time','air_time']])

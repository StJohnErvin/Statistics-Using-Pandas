import pandas as pd

f_usage = [5,4,3,5,8,2,5,2,5,8,10,8,7,9,10,5,7,5,7,5,4,3,5,8,4]

ser = pd.Series(f_usage)
sum_stat = ser.describe()
pstdeviation = ser.std(ddof=0)


print(sum_stat)
print(pstdeviation)

df = pd.read_csv("population_by_country_2020.csv")

df

first_rows = df.head(10)
first_rows

last_rows = df.tail(10)
last_rows

sel_country = df[df["Country"] == "Philippines"]
sel_country

sea =  df[df["Country"].isin(["Philippines","Thailand","Indonesia","Myanmar","Laos","Vietnam","Brunei","Singapore","Malaysia","Cambodia", "Timor-Leste"])]
sea

stat = sea["Population (2020)"].describe()

rstat = round(stat,2)

rstat

import pandas as pd
data = pd.read_csv("datos_energia.csv")
data = data.set_index(pd.DatetimeIndex(data['time']))
data['time']= pd.to_datetime(data['time'])

print(data.dtypes)

print(data.index.date)
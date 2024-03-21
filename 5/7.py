import pandas as pd

data = pd.read_csv('bikes.csv')

res = data['Rachel1'].sum()
print(res)

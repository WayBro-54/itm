# %matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')  # Красивые графики
plt.rcParams['figure.figsize'] = (15, 5)  # Размер картинок
df = pd.read_csv('bikes.csv', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')

df.plot(figsize=(15, 10))
weather_mar2012 = pd.read_csv( skiprows=15, parse_dates=True, encoding='latin1', header=0)
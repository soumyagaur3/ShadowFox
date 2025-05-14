#data preparation
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

df = pd.read_csv('delhiaqi.csv', parse_dates=['date'])

print(df.info())
print(df.describe())

print(df.isnull().sum())

#Time Series Analysis
df.set_index('date', inplace=True)

plt.figure(figsize=(15, 20))
for i, col in enumerate(df.columns, 1):
    plt.subplot(4, 2, i)
    plt.plot(df[col])
    plt.title(col)
    plt.tight_layout()
plt.show()

#Pollutant Correlations
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Pollutant Correlation Matrix')
plt.show()

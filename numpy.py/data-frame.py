import pandas as pd

#df = pd.read_csv('fraud_data.csv')
df = pd.DataFrame({
    'Name': ['John', 'Anna', 'Peter'],
    'Age': [15,25,20],
    'City': ['New York', 'Los Angeles', 'Chicago'],})

#print(df.info())
#print(df.head())
#print(df.tail())
#print(df.describe())
#print(df['Age'] > 15)
#print(df[df['Age'] > 15])
print(df.sort_values(by='Age', ascending=False))

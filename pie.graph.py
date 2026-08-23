import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Daily Household Transactions.csv')
plt.figure(figsize=(10, 6))
plt.pie(df['Amount'], labels=df['Category'], autopct='%1.1f%%', startangle=140, colors=['yellow', 'brown', 'skyblue', 'lightgreen', 'orange'])
plt.title('Daily Household Transactions Distribution')
plt.axis('equal')
plt.show()

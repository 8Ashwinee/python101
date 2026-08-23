import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Daily Household Transactions.csv')
plt.figure(figsize=(10, 10))
plt.plot(df['Date'], df['Amount'], marker='o', linestyle='-', color='red', alpha=0.6)
plt.title('Daily Household Transactions Over Time')
plt.xlabel('Date')
plt.ylabel('Transaction Amount') 
plt.show()
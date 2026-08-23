import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Daily Household Transactions.csv')
plt.figure(figsize=(10, 6))
plt.hist(df['Amount'], bins=30, color='green', edgecolor='brown', alpha=0.6)
plt.title('Daily Household Transactions Amount Distribution')
plt.xlabel('Transaction Amount')
plt.ylabel('Frequency')
plt.show()
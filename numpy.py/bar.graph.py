import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Daily Household Transactions.csv')
plt.figure(figsize=(10, 6))
plt.bar(df['Category'], df['Amount'], color='skyblue', edgecolor='brown', alpha=0.6)
plt.title('Daily Household Transactions')   
plt.xlabel('Category')
plt.ylabel('Transaction Amount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [150, 200, 250, 300, 350]

plt.figure(figsize=(6, 6))

plt.fill_between(months, sales, color='skyblue', alpha=0.4)
plt.plot(months, sales, marker='o', color="black", linewidth=2, alpha=0.7)
plt.title('sales over months')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.show()
#area chart!!!!!!!!!!!!!

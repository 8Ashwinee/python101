import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [150, 200, 250, 300, 350]
plt.figure(figsize=(6, 6))
plt.pie(sales, labels=months, autopct='%1.2f%%', startangle=45, colors=['yellow', 'brown', 'skyblue', 'lightgreen', 'orange'])
plt.title('Sales Distribution')    
#plt.axis('equal')
plt.show()
# pie chart!!!!!!!!!!!!!!



import matplotlib.pyplot as plt

scores = [10, 25, 30, 35, 52, 64, 70, 72, 75, 90]
plt.figure(figsize=(6, 6))
plt.plot(scores, marker='o', color='green', linewidth=2, alpha=0.7)
plt.title('Result of recent exam')
plt.xlabel('Index')
plt.ylabel('Scores')
plt.show()
#line chart!!!!!!!!!!!

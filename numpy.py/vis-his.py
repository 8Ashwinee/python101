import matplotlib.pyplot as plt

scores = [10, 25, 30, 35, 50, 64, 70, 72, 75, 100]
plt.figure(figsize=(6, 6))
plt.hist(scores, color='skyblue', edgecolor='brown', alpha=0.6)
plt.title('Result of recent exam')          
plt.xlabel('Scores')
plt.ylabel('Number of Students')
plt.show()
#histogram!!!!!!!!!!!!!
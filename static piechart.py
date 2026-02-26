import matplotlib.pyplot as plt

labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [40, 25, 20, 15]
colors = ['#4CAF50', '#2196F3', '#FF9800', '#9C27B0']
explode = (0.1, 0, 0, 0) 


plt.figure(figsize=(6,6))
plt.pie(sizes, 
        labels=labels, 
        colors=colors, 
        autopct='%1.1f%%', 
        startangle=140,
        explode=explode)

plt.title('Programming Language Popularity')
plt.axis('equal')  

plt.show()

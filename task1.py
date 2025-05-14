#Matplotib
#1 Line plot
import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[10,20,25,30]
plt.plot(x,y)
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

#2 Scatter plot
x = [1, 2, 3, 4]  
y = [10, 20, 25, 30]  
plt.scatter(x, y)  
plt.title("Scatter Plot")  
plt.show()  

#3 Bar plot
categories = ['A', 'B', 'C']  
values = [5, 7, 3]  
plt.bar(categories, values)  
plt.title("Bar Chart")  
plt.show()  

#4 Histogram
data = [1, 2, 2, 3, 3, 3, 4]  
plt.hist(data, bins=4)  
plt.title("Histogram")  
plt.show()  

#5 Pie chart
sizes = [15, 30, 45, 10]  
labels = ['A', 'B', 'C', 'D']  
plt.pie(sizes, labels=labels, autopct='%1.1f%%')  
plt.title("Pie Chart")  
plt.show()  

#Seaborn
#1 Line plot 
import seaborn as sns  
import matplotlib.pyplot as plt  
sns.lineplot(x=[1, 2, 3, 4], y=[10, 20, 25, 30])  
plt.title("Seaborn Line Plot")  
plt.show()  

#2 Scatter Plot
sns.scatterplot(x=[1, 2, 3, 4], y=[10, 20, 25, 30], hue=["A", "B", "A", "B"])  
plt.title("Seaborn Scatter Plot")  
plt.show()  

#3 Bar plot
sns.barplot(x=["A", "B", "C"], y=[5, 7, 3])  
plt.title("Seaborn Bar Plot")  
plt.show()  

#4 Histogram
sns.histplot(data=[1,2,2,3,4,5,5,5], bins=5, kde=True)  
plt.title("Seaborn Histogram")  
plt.show()  


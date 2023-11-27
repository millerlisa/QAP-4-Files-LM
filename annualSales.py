# QAP 4 Bonus Problem
# Program to enter total monthly sales for the purpose of creating a graph
# Written by Lisa Miller
# Written on November 27, 2023

# Question for Mo: How do I get rid of the extra labels on the x-axis?

# Imports
import matplotlib.pyplot as plt
import matplotlib.style as style    

# Variables
monthLst = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# Create list for x and y axis
Month = []
Total_Monthly_Sales = []
for month in monthLst:
    monthlySales = float(input("Enter the total sales for " + month + ": "))
    Month.append(month)
    Total_Monthly_Sales.append(monthlySales)  
print(Month)
print(Total_Monthly_Sales)
# Create graph
style.use("ggplot")
fig, ax = plt.subplots()
ax.bar(Month, Total_Monthly_Sales, color = "blue")  
plt.title("Total Monthly Sales")
plt.show()

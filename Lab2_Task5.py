# Student Name : Aayush Singh
# Roll_Number : 2024ug3024
# Course : B.Tech CSE DS AI
# Task 5 : Create a list of sales Data for the past 12 months (e.g., sales figures in thousands, caluculate the total sales, average Sales , and the month with the Highest Sales using loops use matplotlib to plot the monthly sales and highlight the month with the highest sales using loops. use matplotlib to plot the monthly sales and the highlight the month with the highest sales)

import matplotlib.pyplot as plt

sales_data = [25,89,28,2,12,23,78,23,31,53,64,63]
total_sales = 0

for i in sales_data:
  total_sales += i

print("Total yearly sales: ", total_sales)

average_sales = total_sales/12
print("Average yearly sales: ", average_sales)

highest_sales = 0
for i in sales_data:
    if(highest_sales<i):
      highest_sales=i

print("Highest Sales: ", highest_sales)

plt.plot(sales_data,marker='x')
plt.xticks(range(1,len(sales_data)+1))
plt.xlabel("Month")
plt.ylabel("sales")
plt.title("MONTH WISE EARLY SALES OF 2024")
plt.show()

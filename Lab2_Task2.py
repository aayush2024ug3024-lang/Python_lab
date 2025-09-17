# Student Name : Aayush Singh
# Roll_Number : 2024ug3024
# Course : B.Tech CSE DS AI
# Task 2 : Write a task to create a python program to print multiplication table from 1 to 12

num1 = 0
num2 = 1

print("Tables from 1 to 12 are: \n")

while(num1 < 12):
    num1 = num1 + 1
    num2 = 1
    while(num2 <=10):
        print(str(num1) + "*" + str(num2)+ "=" + str(num1*num2)  )
        num2 = num2 + 1
   
    print("\n")
   

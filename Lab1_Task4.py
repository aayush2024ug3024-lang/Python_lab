# Student Name : Aayush Singh
# Roll_Number : 2024ug3024
# Course : B.Tech CSE DS AI
# Task : Input two Complex Numbers and display their sum, difference and product


num1_real = int(input("Enter the real part of first number : "))
num1_img = int(input("Enter the complex part of first number : "))
num2_real = int(input("Enter real part of second number : "))
num2_img= int(input("Enter the Complex part of  second number : "))

num1 = complex(num1_real, num1_img)
num2 = complex(num2_real, num2_img)

sum = num1 + num2
difference = num1 - num2
pdt = num1 * num2

print("sum of complex numbers is : ", sum)
print("difference of complex numbers is : ", difference)
print("product of complex numbers is : ", pdt)
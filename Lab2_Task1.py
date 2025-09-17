# Student Name : Aayush Singh
# Roll_Number : 2024ug3024
# Course : B.Tech CSE DS AI
# Task 1 : To Create a python program to classify user according to age


age = input("Enter your age: ")

if age.isnumeric():
    age = float(age)
    if age < 0:
        print("Invalid age!! enter a positive number ")
    elif age < 18:
        print("You are a minor")
    elif age <= 65:
        print("You are an adult")
    else:
        print("You are a senior")
else:
    print("Invalid input!! please enter a numeric value")
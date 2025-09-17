# Student Name : Aayush Singh
# Roll_Number : 2024ug3024
# Course : B.Tech CSE DS AI
# Task 3 : Write a task to create a python program to check the strength of a password


num = input("enter you password to check if its safe :")

if len(num) < 8:
    print("Password is too short")
else:
    numeric = False
    lower = False
    upper = False
    special = False
    # for i in num:
    #     if i.isdigit():
    #         numeric = True
    #     elif i.islower():
    #         lower = True
    #     elif i.isupper():
    #         upper = True
    #     elif i in "!@#$%^&*()-+":
    #         special = True
            
    # if numeric and lower and upper and special:
    #     print("Password is strong")
    # else:
    #     print("Password is weak")


    if any(i.isdigit() for i in num):
        numeric = True
    if any(i.islower() for i in num):
        lower = True
    if any(i.isupper() for i in num):
        upper = True
    if any(i in "!@#$%^&*()-+" for i in num):
        special = True

    if numeric and lower and upper and special:
        print("Password is strong")
    else:
        print("Password is weak")

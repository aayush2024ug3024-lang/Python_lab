# Student Name : Aayush Singh
# Roll_Number : 2024ug3024
# Course : B.Tech CSE DS AI
# Task 2 : To implement the grade card of the student

marks=[]

for i in range (5):
    marks.append(float(input("Enter marks of subject " + str(i+1) + ": ")))

total_marks=0

for i in range (5):
    total_marks += marks[i]

def Grade(marks):
    if marks>= 90:
        return 'A'
    elif marks>= 80:
        return 'B'
    elif marks >=70:
        return 'C'
    elif marks >=60:
        return 'D'
    elif marks >=50:
        return 'E'
    else:
        return 'F'
    
    for i in range (5):
        print("Grade Sub" + str(i+1) + ": ", Grade(marks[i]))
    
print("Grade Sub1: ", Grade(marks[0]))
print("Grade Sub2: ", Grade(marks[1]))
print("Grade Sub3: ", Grade(marks[2]))
print("Grade Sub4: ", Grade(marks[3]))
print("Grade Sub5: ", Grade(marks[4]))
print("Average Marks: ", total_marks/5)
print("Grade Overall: ", Grade(total_marks/5))


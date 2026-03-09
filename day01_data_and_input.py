#Day 01 - Data Types & User Input
#Date 9th march 2026

name = "Giovanni Ayiah_Mensah" #String 
age = 20 #integer 
gpa = 3.27 # float
is_student = True #Boolean 

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

print("")

num1 = "5"
num2 = "3"
print(num1 + num2)

num3 = 5
num4 = 3

print(num3 + num4)

name = input("What is your name?")
age = int(input("How old are you ?"))
gpa = float(input("What is your CGPA ?"))

#print(f"\nHello {name}!!")
#print(f"You are {age} years old.")
#print(f"Your CGPA is {gpa}.")
#print(f"In 5 years you will be {age + 5} years old.")
#print(f"Keep pushing {name} You've got this 🔥")

name = input("Enter your name:")
age = int(input("Enter your age:"))
gpa = float(input("Enter your GPA:"))
course = input("Enter your course:")
university = input("Enter your University:")

print("\n==============================================")
print("                 STUDENT PROFILE                ")
print(f"Name:                {name} ")
print(f"Age:                 {age} ")
print(f"GPA:                 {gpa} ")
print(f"Course:              {course} ")
print(f"University           {university} ")
print("=================================================")
print(f"Keep Pushing {name}!! Your future is 🔥         ")
print("==================================================")

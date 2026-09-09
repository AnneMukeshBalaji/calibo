# Write a python program to enter a Radius of Circle  and find the area

# import math
# def compute_area(radius) -> float:
#     return math.pi * radius ** 2;
# radius = float(input())
# print(compute_area(radius))

# Write a python program that takes student id , student name and three subject marks and dispaly total , avaryage and report of the student 

# student_id = int(input("Enter You're Id : "))
# student_name = input("Enter You're Name : ")
# subject1_marks = int(input("Enter subject1 Marks : "))
# subject2_marks = int(input("Enter Subject2 Marks : "))
# subject3_marks = int(input("Enter Subject3 Marks : "))
# total_marks = subject1_marks + subject2_marks + subject3_marks
# average_marks = total_marks / 3 
# print(f"Student_ID : {student_id}\nStudent_Name : {student_name}\nTotal_Marks : {total_marks}\nAverage_Marks : {average_marks}")
#
# if subject3_marks > 40 and subject1_marks > 40 and subject2_marks > 40 : 
#     print('Pass') 
#     if average_marks <= 50 and average_marks >= 40 :
#         print('Grade C')
#     elif average_marks >= 50 and average_marks <= 60 :
#         print('Grade B')
#     elif average_marks >= 60 and average_marks <= 70 :
#         print('Grade A')
#     else :
#         print('Student Passed in Distinction')
# else : 
#     print('Fail')

# i = 1
# sum = 0
# n = int(input("Enter n Value : "))
# while i < n: 
#     sum += i
#     i += 1
# print(sum)

# n = int(input())
# i = 1
# fact = 1 
# if n > 0 :
#     while i  < n :
#         fact *= i
#         i += 1
#     print(fact)
# else :
#     if n == 0 :
#         print(1)
#     else : 
#         print(-1)

for i in range(1,11): # starting value , ending value , step value 
    print(i)

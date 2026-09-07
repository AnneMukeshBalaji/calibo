# Function is block that contains a specific set of code to solve a specific problem and every variable in the python is block scope except global variables 
# NOTE: To Work with functions you need two things function definition and function calling

# NOTE: 1]Function Definition : 

# PERF:       def function_name(list_of_arguments):
#               function_body

# NOTE: 2]Function Calling : 

# PERF:       function_name(list_of_arguments)

# NOTE: 
#       1)It Accepts the Values 
#       2)It Returns the value

# NOTE: Types of Functions : 
                       
#                       1]Function with no list_of_arguments and no return_value 
#                       2]Function with list_of_arguments and without return_value 
#                       2]Function with no list_of_arguments and with return_value
#                       3]Function with list_of_arguments and  with return_value 

# NOTE: Category 1 
def add1() -> None :
    a = int(input())
    b = int(input())
    print(f'{a+b}')

# NOTE: Category 2
def add2(*list):
    print(sum(list))

# NOTE: Category 3 
def add3():
    pass

def calculate_marks(*ag_list) -> None:
    student_number,student_name,marks1,marks2,marks3 = ag_list
    total_marks = marks1 + marks2 + marks3
    average_marks = total_marks / 3 
    print(f'''Student Number: {student_number}\nStudent Name: {student_name}\nSubject1 Marks: {marks1}\nSubject2 Marks: {marks2}\nSubject3 Marks: {marks3}\nTotal Marks: {total_marks}\nAverage Marks: {average_marks}''')

def main() -> None:
    student_number = int(input("Enter Student Number : "))
    student_name = input("Enter Student Name : ")
    marks1 = int(input("Enter Subject1 Marks : "))
    marks2 = int(input("Enter Subject2 Marks : "))
    marks3 = int(input("Enter Subject3 Marks : "))
    calculate_marks(student_number,student_name,marks1,marks2,marks3)
if __name__ == "__main__":
    main()

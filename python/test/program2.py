# Write a Python program using sets to analyze the course enrollments.
# Given Data:
# python_students = {"Rahul", "Priya", "Anil", "Sneha", "Kiran"}sql_students = {"Priya", "Anil", "Meghana", "Kiran", "Arjun"}java_students = {"Anil", "Sneha", "Kiran", "Arjun", "Ravi"}
# Requirements:
# Display the students enrolled in both Python and SQL.
# Display the students enrolled in Python but not SQL.
# Display the students enrolled in at least one course.
# Display the students enrolled in all three courses.
# Display the students enrolled in exactly one course.
# Display the total number of unique students across all courses.
def print_students_in_both(a,b) -> None:
    print("Students who are enrolled in both Python and SQL : ")
    for i in a :
        if i in b : 
            print(i)


def print_students_in_a_not_b(a,b) -> None:
    print("Students who are enrolled in Python and not in SQL : ")
    for i in a :
        if i not in b :
            print(i)


def print_students_enrolled_in_atleat_one(a,b,c) -> None:
    print("Students who are enrolled in atleast one Course : ")
    for i in a :
        print(i)
    for i in b :
        if i not in a :
            print(i)
    for i in c :
        if i not in a and i not in b :
            print(i)


def print_students_in_all_3(a,b,c) -> None:
    print("Students who are enrolled in Python,SQL, and in Java  : ")
    for i in a :
        if i in b :
            if i in c :
                print(i)


def print_students_in_one_coures(a,b,c) -> None:
    print("Students who are enrolled in only one Course : ")
    for i in a :
        if i not in b and i not in c :
            print(i)
    for i in b:
        if i not in a and i not in c :
            print(i)
    for i in c:
        if i not in a and i not in b:
            print(i)


def count_of_unique_students(a,b,c) -> None:
    print("Total Count of Unique Students : ")
    count = 0
    for i in a :
        count += 1
    for i in b :
        if i not in a :
            count += 1
    for i in c :
        if i not in a and i not in b :
            count += 1
    print(count)

def main() -> None:
    python_students = {"Rahul", "Priya", "Anil", "Sneha", "Kiran"}
    sql_students = {"Priya", "Anil", "Meghana", "Kiran", "Arjun"}
    java_students = {"Anil", "Sneha", "Kiran", "Arjun", "Ravi"}
    print_students_in_both(python_students,sql_students)
    print_students_in_a_not_b(python_students,sql_students)
    print_students_enrolled_in_atleat_one(python_students,sql_students,java_students)
    print_students_in_all_3(python_students,sql_students,java_students)
    print_students_in_one_coures(python_students,sql_students,java_students)
    count_of_unique_students(python_students,sql_students,java_students)
if __name__ == "__main__":
    main()

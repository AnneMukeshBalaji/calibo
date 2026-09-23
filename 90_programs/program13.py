"""
Write a python program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. Calculate percentage and grade according to following:
Percentage >= 90% : Grade A
Percentage >= 80% : Grade B
Percentage >= 70% : Grade C
Percentage >= 60% : Grade D
Percentage >= 40% : Grade E
Percentage < 40% : Grade F
"""
def display_grade(physics_marks:int,chemistry_marks:int,biology_marks:int,math_marks:int,computer_marks:int) -> None :
    total_marks = physics_marks + chemistry_marks + biology_marks + math_marks + computer_marks
    percentage = (total_marks / 500) * 100
    if percentage >= 90 :
        print("Grade A")
    elif percentage >= 80 :
        print("Grade B")
    elif percentage >= 70 :
        print("Grade C")
    elif percentage >= 60:
        print("Grade D")
    elif percentage >= 40:
        print("Grade E")
    else :
        print("Grade F")
def main() -> None:
    physics_marks = int(input("Enter Physics Marks : "))
    chemistry_marks = int(input("Enter Chemistry Marks : "))
    biology_marks = int(input("Enter Biology Marks : "))
    math_marks = int(input("Enter Mathematics Marks : "))
    computer_marks = int(input("Enter Computer Marks : "))
    display_grade(physics_marks,chemistry_marks,biology_marks,math_marks,computer_marks)
if __name__ == "__main__":
    main()

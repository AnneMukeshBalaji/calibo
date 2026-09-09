# Write a program to remove the dulicate values in the list 
# input : [4,-6,-6,6,6,-2,-9,2]
# output : [4,-6,6,-2,-9,2]
def remove_duplicates(a) -> list:
    output_list = []
    for i in a :
        if i not in output_list:
            output_list.append(i)
    return output_list
def main() -> None:
    a = [4,-6,-6,6,6,-2,-9,2]
    print('Before Removing Duplicates : ',a)
    a = remove_duplicates(a)
    print('After Removing Duplicates : ',a)
if __name__ == "__main__":
    main()

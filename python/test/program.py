# Write a program on list 
# input : [4,-6,6,-2,-9,2]
# output : [-6,-2,-9,4,6,2]
def print_output(a) -> None:
    output_list = []
    for i in a :
        if i < 0 :
            output_list.append(i)
    for i in a :
        if i >=0 :
            output_list.append(i)
    print(output_list)
def main() -> None:
    a = [4,-6,6,-2,-9,2]
    print_output(a)
if __name__ == "__main__":
    main()

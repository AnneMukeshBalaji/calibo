# Write a python script to accept a list from keyboard and display list elements 
def main() -> None:
    my_list = []
    list_size = int(input('Enter The size of the List : '))
    for _ in range(list_size):
        val = int(input(f'Enter {_ + 1} value : '))
        my_list.append(val)
    print(my_list)
    print(max(my_list))
    print(min(my_list))
    print(max_value_index(my_list))
def max_value_index(list_value) -> int:
    index = 0
    for i in range(1,len(list_value)):
        if list_value[index] < list_value[i]:
            index = i
    return index
if __name__ == "__main__":
    main()

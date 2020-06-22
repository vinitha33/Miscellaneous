#02 June 2020

# Declare a list containing int/str/float values . Write a code to iterate the list and store
# those values into 3 different lists one for int, one for str and one list for float values

def lists(list1):
    print("*********1**********")
    int_list= []
    str_list = []
    float_list = []
    for i in list1:
        if type(i) == int:
            int_list.append(i)
        elif type(i) == float:
            float_list.append(i)
        else:
            str_list.append(i)
    print("Integer list:", int_list)
    print("Float list:", float_list)
    print("String list:", str_list)


# lists([1, 'apple', 2, 3.3, 'banana', 4, 5, 4.6, 'cherry'])

def cube():
    print("\n*********2**********")
    while True:
        num = input("Enter the number (q to exit):")
        if num == 'q':
            break
        print(pow(int(num), 3))

# cube()
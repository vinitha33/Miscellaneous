# Date - 01 June 2020
# Write a program to find multiplication table of a number 7

def multi_table(num):
    print("*********1**********")
    i = 1
    while i <= 10:
        print(num, "X", i, "=", i * num)
        i += 1


# multi_table(7)

# Declare the list [-4,3,1,6,-7,0,-9,-1,5]
# Write a script to get to the count of negative, positive values from list

def posneg(list1):
    print("\n*********2**********")
    pos = 0
    neg = 0
    zero = 0
    for i in list1:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zero += 1
    print("Number of positive values in the list are:", pos)
    print("Number of negative values in the list are:", neg)
    print("Number of zeroes in the list are:", zero)

# posneg([-4,3,1,6,-7,0,-9,-1,5])
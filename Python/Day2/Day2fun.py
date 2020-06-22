# Date - 29 May 2020
# Write a code to print the below pattern


def pattern(num):
    print("*********1**********")
    for i in num:
        print(str(i) * i)
        i = i - 1


# pattern([5,4,3,2,1])


# Declare a list range(533,875). Try to count the number of odd and even numbers between
# the above range

def odd_even(list1):
    print("\n*********2**********")
    odd = 0
    even = 0
    for i in list1:
        if i%2 == 0:
            even += 1
        else:
            odd += 1
    print("Count of odd numbers are:", odd)
    print("Count of odd numbers are:", even)


# odd_even(range(533,875))
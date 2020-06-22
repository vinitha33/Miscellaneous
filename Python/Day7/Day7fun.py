# 10 June 2020
# ------------------1-----------------------
# Write a program which will find all such numbers which are divisible by 7 but are not a
# multiple of 5, between 5000 and 7500 (both included).




def divisibilitycheck(num1, num2):
    '''
    Returns the numbers between range 5000 and 7000 which are divisible by 7 and not divisible by 5
    :param

        num1 (int) : An integer from where the value is to be taken
        num2 (int) : An integer till where the value is to be considered

    :return:
        res (list) : An output variable which displays the divisible numbers
    '''
    res = []
    for x in range(num1, num2 + 1):
        if x % 7 == 0 and x % 5 != 0:
            res.append(str(x))

    print("res(numbers divisible by 7 and not 5 are: ", ','.join(res))


# print(divisibilitycheck.__doc__)

# divisibilitycheck(5000, 7500)


# ---------------------2------------------------

'''
2)
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.

Suppose the following input is supplied to the program:

34,67,55,33,12,98

Then, the output should be:

['34', '67', '55', '33', '12', '98']

('34', '67', '55', '33', '12', '98')'''

def listtuple(str1):
    '''
    Takes input CSV's and print generates a list and tuple of the same values
    :param
        str1 (string): The comma separated values taken as input from the user

    :return:
        list2 (list): A list containing the values from the CSV input
        tuple1 (tuple): A tuple containing the values from the CSV input
    '''
    list2 = []
    tuple1 = ()
    list1 = str1.split(",")
    for i in list1:
        list2.append(int(i))
        tuple1 = tuple(list2)
    print("List:", list2)
    print("Tuple:", tuple1)


# print(listtuple.__doc__)
# listtuple(input("Enter the string:"))

# ----------------------3-----------------------------

'''
3) Write a code to generate the Fibonacci series (val<200)
'''




def fibonacci(num):
    '''

    :param
        num (int): An integer value upto which the fibonacci series is to be found out

    :return:
        n1 (inr) : A sequence of fiboacci series
    '''
    n1, n2 = 0, 1
    count = 0

    if num <= 0:
        print("Enter a positive integer:")
    elif num == 1:
        print("Fibonacci upto", num, ":")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < num and n1 < 200:
            print(n1)
            num1 = n1 + n2
            n1 = n2
            n2 = num1
            count += 1


# print(fibonacci.__doc__)
# fibonacci(int(input("Enter the num till which you want the fibonacci series:")))

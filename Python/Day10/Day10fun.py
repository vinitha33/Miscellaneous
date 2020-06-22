# Functions takes two inputs , first input is mandatory, if second is not there use 1,
# else if 0 raise error.

print("********1********")
def fun1(a,b = 1):
    '''
    :param
     a (int): An integer value
    :param
     b: (int): An integer value
    :return:
        Returns an error if the value of b given by user is 0
    '''

    if b == 0:
        print("Error")
    else:
        print("a = ", a)
        print("b = ", b)

print(fun1.__doc__)
fun1(10)
fun1(10,0)


# swapcase a string without using built in functions


print("********2********")


def swapcase(str1):
    '''
    :param
     str1 (string): A string value
    :return:
        Returns a swapcased value of the string taken an input
    '''

    swap = ""
    for i in str1:
        if i.isupper():
            swap += i.lower()
        else:
            swap += i.upper()
    print("String after swapping case:", swap)


print(swapcase.__doc__)
swapcase(input("Enter the string which is to be swapcased:"))


# Write a function called is_abecedarian that returns True if the letters in a word appear
# in alphabetical order (double letters are ok). How many abecedarian words are there? (i.e)
# "Abhor" or "Aux" or "Aadil" should return "True" Banana should return "False"

print("********3********")


def is_abecedarian(str1):
    '''
    :param
     str1 (string): A string value
    :return:
    Returns True if the string value taken as input is ordered alphabetically, False otherwise
    '''

    str2 = sorted(str1)
    str3 = "".join(str2)
    if str3.lower() == str1.lower():
        return True
    else:
        return False


print(is_abecedarian.__doc__)
print(is_abecedarian(input("Enter the string:")))


# Write a function to convert Celsius to Fahrenheit and vice versa

print("********4********")

def C2F(c):
    '''
    :param
     c (float): An integer value (Celsius)
    :return:
     f (float) : Value of fahrenheit corresponding to the celsius taken as input
    '''
    f = (c * 1.8) + 32
    print("Fahrenheit is:{:.2f}".format(f))

def F2C(f):
    '''
    :param
     f (float): An integer value (Fahrenheit)
    :return:
     c (float) : Value of celsius corresponding to the fahrenheit taken as input
    '''
    c = (5 / 9) * (f - 32)
    print("Celsius is:{:.2f}".format(c))




print("Enter your choice?")
while True:
    choice = int(input("1. Celsius to Fahrenheit \n2. Fahrenheit to Celsius"))
    if choice != 1 and choice != 2:
        print("Not a valid choice")
        break
    elif choice == 1:
        print(C2F.__doc__)
        c = float(input("Enter Celsius:"))
        C2F(c)
    else:
        print(F2C.__doc__)
        f = float(input("Enter Fahrenheit:"))
        F2C(f)


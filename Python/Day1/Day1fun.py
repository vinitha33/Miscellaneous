# Date - 28 May 2020
# Check if 'coffee' is present in the stringstr1 = "I drink coffee every morning"


def findword(str1):
    print("*********1**********")
    sub = "coffee"
    if sub in str1:
        print("Coffee is present in the string")
    else:
        print("No")


#findword("I drink coffee every morning")

# print the alphabet after the first occurrence of ',' from the below String
# 'I like python ,Perl scripting'


def findalpha(str1):
    print("*********2**********")
    str2 = str1.find(',')
    print(str1[str2 + 1])


# findalpha("I like python ,Perl scripting")

# get your full name and convert the first and middle name as abbreviations
# example : Sakthi Vinoth Ramadoss --> S.V.Ramadoss


def abbre(str1):
    print("*********3**********")
    list2 = str1.split()
    print(list2[0][0] + "." + list2[1][0] + "." + list2[2])


# abbre("Vinitha Muralidharan Nair")

# count the no. of whitespaces --> ": vect1 and vect2 are lists of equal length of numbers"


def countwhitespace(str1):
    print("*********4**********")
    print(str1[0].count(" "))


# countwhitespace([": vect1 and vect2 are lists of equal length of numbers"])

# I have a string -> str1 = "PYnative" - Use Slicing to get the output something like this
# --> Yna PYnat tive PYnativ PYnativ


def slicing(str1):
    print("*********5**********")
    print(str1[1:4] + " " + str1[:5] + " " + str1[4:] + " " + str1[:-1] + " " + str1[:7])


# slicing("PYnative")



# 09 June 2020

'''1)
def sumDigits(s):
         """Assumes s is a string
         Returns the sum of the decimal digits in s
         For example, if s is 'a2b3c' it returns 5"""'''
def sumDigits(s):
    sum = 0
    for i in s:
        if i.isdigit():
            sum += int(i)
    print("Sum is:", sum)

# print("*********1*********")
# sumDigits(input("Enter the string (combination of digits & alphabets):"))

'''
2) def isPalindrome(s):
         """Assumes s is a str
         Returns True if s is a palindrome; False otherwise.
         Punctuation marks, blanks, and capitalization are
         ignored."""'''


def isPalindrome(s):
    str1 = ""
    for i in range(len(s)):
        if s[i].isalpha():
            str1 += s[i]
    str2 = str1[::-1]
    if str1.lower() == str2.lower():
        return True
    else:
        return False

# print("*********2*********")
# print(isPalindrome(input("Enter the string:")))


'''
3) Write a program that computes the decimal equivalent of the binary number 10011?
'''

def binary2decimal(num):
    i = 0
    final = 0
    if '1' not in str(num) or '0' not in str(num):
        print("Not a valid binary number")
    else:
        while num > 0:
            rem = num % 10
            num = round(num / 10)
            digit = pow(2, i) * rem
            final = final + digit
            i += 1
        print(final)

# binary2decimal(102)
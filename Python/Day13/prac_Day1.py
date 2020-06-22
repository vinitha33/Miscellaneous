#Date - 17/06

list1 = [[1,2,3],4,[5,6]]
sum = 0

for i in range(len(list1)):
    # if type(list1[i]) == list:
    if isinstance(list1[i], list):
        for j in range(len(list1[i])):
            sum = sum + list1[i][j]
    else:
        sum = sum + list1[i]

print("Sum is:", sum)




# str1 = "aBcDEFz"
# str2 = ''
# for i in range(len(str1)):
#     while ord(str1[i]) > 96 and ord(str1[i]) < 123:
#         str2 += chr(ord(str1[i]) - 32)
#         break
#     while ord(str1[i]) > 64 and ord(str1[i]) < 91:
#         str2 += chr(ord(str1[i]) + 32)
#         break
# print(str2)





'''
str1 = "I am doing well"
abcd = {}
for i in str1:
    if i in abcd:
        abcd[i] += 1
    else:
        abcd[i] = 1
print(abcd)
'''


# str1 = "Vinitha0303"
# list1 = []
# for i in range(len(str1)):
#     if str1[i].isdigit():
#         list1.append(str1[i])
#
# str2 = "".join(list1)
# print(str2)


'''
vowel_set = {"a", "e", "i", "o", "u"}
str1 = "mango"
num = 0
count = 0
str1.lower()
for i in range(len(str1)):
    if str1[i] not in vowel_set:
        num += 1
    if num > count:
        count = num
    if str1[i] in vowel_set:
        num = 0

print(count)
'''

# for i in range(1, 6):
#     print(' '*(6 - i), '*'*(i * 2 - 1))



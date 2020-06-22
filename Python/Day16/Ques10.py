str1 = "I am reading a book"
vowel_set = {'a', 'e', 'i', 'o', 'u'}
list1 = str1.split()
c = 0
z = 0
C = []
str2 = ''

for i in range(len(list1)):
    c = 0
    for j in range(len(list1[i])):
        if list1[i][j] in vowel_set:
            c = c + 1

    C.append(c)

for i in range(len(C)):
    str2 = ''
    z = 0
    for j in range(len(C)):
        if C[i] > C[j]:
            z = C[i]
            C[i] = C[j]
            C[j] = z
            str2 = list1[i]
            list1[i] = list1[j]
            list1[j] = str2

str3 = ' '
str3 = str3.join(list1)

print(str3)
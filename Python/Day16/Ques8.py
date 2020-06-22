
def long_alpha(str1):
    list1 = []
    list2 = ""
    maxi = 0
    j = 0
    for i in range(len(str1)):
        if i == 0:
            list2 += str1[i]
        elif ord(str1[i - 1]) <= ord(str1[i]):
            list2 += str1[i]
        else:
            list1.append(list2)
            list2 = ""
            list2 += str1[i]
    list1.append(list2)

    for i in range(len(list1)):
        if maxi < len(list1[i]):
            maxi = len(list1[i])
            j = i
    return list1[j]
str1 = "abcaklmoeeffd"
res = long_alpha(str1)
print(res)

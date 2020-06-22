def max_pali(str1):
    maxi = 0
    for i in range(len(str1)):
        for j in range(len(str1)):
            if str1[i] == str1[j] and i != j:
                count = 0
                str2 = ""
                for k in range(i, j + 1):
                    # print(str1[k])
                    str2 += str1[k]
                    # str3 = str2[::-1]
                if str2 == str2[::-1]:
                    count = len(str2)
                if maxi < count:
                    maxi = count
    return maxi

str1 = "cabbagemalayalamadam"
res = max_pali(str1)
print(res)

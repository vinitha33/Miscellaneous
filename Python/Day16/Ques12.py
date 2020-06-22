str1 = "cabbagemalayalamadam"
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
print(maxi)




# i = 0
# count = 0
# max = 0
# j = len(str1) - 1
# while i < len(str1):
#     let = str1[i]
#     if let == str1[j]:
#         count += 1
#         i += 1
#         j -= 1
#         if max < count:
#             max = count
#     else:
#         j -= 1
#
# print(max)
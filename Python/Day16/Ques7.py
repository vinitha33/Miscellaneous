list1 = ["eat", "tea", "far", "raf", "arf"]
list3 = []
for i in range(len(list1)):
    str1 = sorted(list1[i])
    list2 = []
    for j in range(len(list1)):
        if str1 == sorted(list1[j]):
            list2.append(list1[j])
            list1.remove(list1[j])
            j -= 1
    list3.append(list2)
print(list3)



def is_palindrome(str1):
    j = len(str1) - 1
    c = 0
    for i in range(int(len(str1) / 2)):
        if str1[i] != str1[j]:
            c = 1
        j = j - 1
    if c == 1:
        return False
    else:
        return True


    # if len(str1) % 2 != 0:
    #     mid = int(len(str1) / 2)
    #     flag = flag1 = mid
    #     r_list = []
    #     l_list = []
    #     r_str = l_str = ""
    #     while flag >= 0:
    #         l_list.append(str1[flag])
    #         flag -= 1
    #     l_str = "".join(l_list)
    #     while flag1 < len(str1):
    #         r_list.append(str1[flag1])
    #         flag1 += 1
    #     r_str = "".join(r_list)
    #     if r_str == l_str:
    #         return True
    #     else:
    #         return False
    # else:
    #     mid = int(len(str1) / 2)
    #     flag = flag1 = mid
    #     l_list = []
    #     r_list = []
    #     r_str = l_str = ""
    #
    #     while flag > 0:
    #         l_list.append(str1[flag - 1])
    #         flag -= 1
    #     l_str = "".join(l_list)
    #     while flag1 < len(str1):
    #         r_list.append(str1[flag1])
    #         flag1 += 1
    #     r_str = "".join(r_list)
    #     if l_str == r_str:
    #         return True
    #     else:
    #         return False


str1 = "car"
print(is_palindrome(str1))


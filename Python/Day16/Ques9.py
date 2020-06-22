def count_occur(num):
    num1 = 100110110
    dec = 0
    i = 1
    s = 0
    c = 0
    count = 0
    while num > 0:
        rem = int(num % 2)
        s = s + (i * rem)
        num = int(num/2)
        i = i * 10

    while num1 != 0:
        if num1 % i == s:
            c = c + 1
            num1 = int(num1/10)
        else:
            num1 = int(num1/10)
    return c

num = 5
res = count_occur(num)
print(res)
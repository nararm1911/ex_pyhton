from random import randint

def random_list(n):
    matrix = []
    for i in range(n):
        matrix.append(randint(1000, 10000))
    return matrix

def find_el(list):
    sum_list = []
    for i in list:
        sum_ele = 0
        conv_i = str(i)
        for j in conv_i:
            conv_j = int(j)
            sum_ele += conv_j
        sum_list.append(sum_ele)
    return  sum_list

def buble(list_sum):
    n = len(list_sum)
    for i in range(n):
        for j in range(0, n - i - 1):
            if list_sum[j] > list_sum[j + 1]:
               list_sum[j], list_sum[j + 1] = list_sum[j + 1], list_sum[j]
    return list_sum


a = random_list(10)
print(a)
b = find_el(a)
print(b)
c = buble(b)
print(c)

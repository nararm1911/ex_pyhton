# rom math import factorial

# x = factorial(4)

# print(x)

num = int(input('please insert number  = '))
fact_num = 1
i = 1
while i <= num:
    fact_num *= i
    i = i + 1

print(fact_num)

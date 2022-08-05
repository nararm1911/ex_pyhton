
list_1 = list(input('please input first list = '))
sum_list = 0
prod_list = 1

for i in list_1:
    conv_i = int(i)
    sum_list += conv_i
    prod_list *= conv_i

print(f'list numbers are = {list_1} sum of list = {sum_list}, prod = {prod_list}')


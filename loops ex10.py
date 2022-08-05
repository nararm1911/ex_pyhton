
num_1 = int(input('input first number = '))
num_2 = int(input('input second number = '))
sin = str(input('please enter signs operation like + - * / = '))

while num_1 or num_2 != 0:

    if sin == str('+'):
        sum_num = num_1 + num_2
        print(sum_num)
    elif sin == str('-'):
        sum_min = num_1 - num_2
        print(sum_min)
    elif sin == str('*'):
        sum_prod = num_1 * num_2
        print(sum_prod)
    else:
        sum_div = num_1 / num_2
        print(sum_div)


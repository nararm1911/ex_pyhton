
num_1 = int(input('insert number 1 = '))
num_2 = int(input('insert number 2 = '))


if num_1 == 0 or num_2 == 0:
    print('enter none 0 number')
else:
    div = int(num_1 / num_2)
    r = num_1 - num_2 * div

print(f'the div is {div} and integer part is {r}')




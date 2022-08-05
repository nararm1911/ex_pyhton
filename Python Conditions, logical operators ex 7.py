
num_1 = int(input('insert num1 = '))
num_2 = int(input('insert num2 = '))
num_3 = int(input('insert num3 = '))

if num_1 > num_2 > num_3 or num_1 < num_2 < num_3:
    print(f'average number is {num_2}')
elif num_2 > num_1 > num_3 or num_2 < num_1 < num_3:
    print(f'average number is {num_1}')
else:
    print(f'average number is {num_3}')




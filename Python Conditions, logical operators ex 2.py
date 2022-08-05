
num_1 = int(input('num 1  = '))
num_2 = int(input('num 2  = '))
num_3 = int(input('num 3  = '))

if num_1 > num_2 and num_1 > num_3:
    print(f'biggest number is {num_1}')
elif num_2 > num_1 and num_2 > num_3:
    print(f'biggest number is {num_2}')
else:
    print(f'biggest number is {num_3}')

